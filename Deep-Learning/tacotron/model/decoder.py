import torch
from torch import nn
from torch.nn import functional as F
from torch.autograd import Variable
from model.attention import Attention
from model.layers import ConvNorm, LinearNorm
from model.modules import Prenet
from hparams import hparams as hps
from utils import get_mask_from_lengths


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()

        self.n_frames_per_step = hps.n_frames_per_step
        self.n_mel_channels = hps.n_mel_channels
        self.encoder_embedding_dim = hps.encoder_embedding_dim
        self.attention_rnn_dim = hps.attention_rnn_dim
        self.decoder_rnn_dim = hps.decoder_rnn_dim

        self.prenet = Prenet()

        self.attention_rnn = nn.LSTMCell(256 + 512, 1024)
        self.attention_layer = Attention()

        # decoder rnn input : 256 + 512 = 768
        # decoder rnn output : 1024
        self.decoder_rnn = nn.LSTMCell(256 + 512, 1024, 1)

        self.linear_projection = LinearNorm(1024, 80 * 3)


    def get_go_frame(self, memory):
        batch_size = memory.size(0)
        go_frames = Variable(
            memory.data.new(batch_size,
                            self.n_frames_per_step * self.n_mel_channels).zero_())
        return go_frames

    def parse_decoder_inputs(self, decoder_inputs):
        batch_size = decoder_inputs.size(0)
        frame_size = decoder_inputs.size(2)

        decoder_inputs = decoder_inputs.transpose(1, 2).contiguous()
        # print('decoder input transpose : ', decoder_inputs.size())
        decoder_inputs = decoder_inputs.view(batch_size,
                                            int(frame_size / self.n_frames_per_step), -1)
        # print('decoder input view : ', decoder_inputs.size())
        decoder_inputs = decoder_inputs.transpose(0, 1)
        # print('decoder input transpose : ', decoder_inputs.size())
        return decoder_inputs

    def parse_decoder_outputs(self, mel_outputs):
        # List[(B, 240) ....] -> (len(List) : 278, B, 240)
        mel_outputs = torch.stack(mel_outputs)
        # print(mel_outputs.size())
        mel_outputs = mel_outputs.transpose(0, 1).contiguous()
        # print(mel_outputs.size())
        batch_size = mel_outputs.size(0)
        mel_outputs = mel_outputs.view(batch_size, -1, 80)
        # print(mel_outputs.size())
        mel_outputs = mel_outputs.transpose(1, 2)
        # print(mel_outputs.size())
        return mel_outputs

    def initailze_decoder_states(self, memory, mask):
        batch_size = memory.size(0)
        max_time = memory.size(1)

        self.attention_hidden = Variable(memory.data.new(batch_size, self.attention_rnn_dim).zero_())
        self.attention_cell = Variable(memory.data.new(batch_size, self.attention_rnn_dim).zero_())

        self.decoder_hidden = Variable(memory.data.new(batch_size, self.decoder_rnn_dim).zero_())
        self.decoder_cell = Variable(memory.data.new(batch_size, self.decoder_rnn_dim).zero_())

        self.attention_weights = Variable(memory.data.new(batch_size, max_time).zero_())
        self.attention_weights_cum = Variable(memory.data.new(batch_size, max_time).zero_())
        self.attention_context = Variable(memory.data.new(batch_size, self.encoder_embedding_dim).zero_())

        # (B , seq_len, 512)
        self.memory = memory
        # (B , seq_len, 128)
        self.processed_memory = self.attention_layer.memory_layer(memory)
        self.mask = mask

    def decode(self, decoder_input):
        # decoder input : (B, 256)
        # attention context : (B, 512)
        # attention cell input : (B, 256+512)
        attention_cell_input = torch.cat((decoder_input, self.attention_context), dim=-1)
        print('attention cell input : ', attention_cell_input.size())
        # attention_hidden : (B, 1024)
        # attention_cell : (B, 1024)
        self.attention_hidden, self.attention_cell = self.attention_rnn(
            attention_cell_input, (self.attention_hidden, self.attention_cell))

        print('attention hidden, cell : ', self.attention_hidden.size(), self.attention_cell.size())

        self.attention_hidden = F.dropout(self.attention_hidden, 0.1, self.training)

        attention_weights_cat = torch.cat(
            (self.attention_weights.unsqueeze(1),
             self.attention_weights_cum.unsqueeze(1)),
             dim=1
        )

        print('attention_weights_cat : ', attention_weights_cat.size())
        print('attention_weights : ', self.attention_weights.size())
        print('attention_weights_cum : ', self.attention_weights_cum.size())

        self.attention_context, self.attention_weights = self.attention_layer(
            self.attention_hidden, self.memory, self.processed_memory,
            attention_weights_cat, self.mask
        )

        return None, None

    def forward(self, memory, decoder_inputs, memory_lengths):
        # memory : (B, Seq_len, 512) --> encoder outputs
        # decoder_inputs : (B, Mel_Channels : 80, frames)
        # memory lengths : (B)

        decoder_input = self.get_go_frame(memory).unsqueeze(0)
        # print('go frames : ', decoder_input.size())
        # print('decoder inputs : ', decoder_inputs.size())
        decoder_inputs = self.parse_decoder_inputs(decoder_inputs)
        decoder_inputs = torch.cat((decoder_input, decoder_inputs), dim=0)
        # print('decoder inputs : ', decoder_inputs.size())
        decoder_inputs = self.prenet(decoder_inputs)

        self.initailze_decoder_states(memory,
                                      mask=~get_mask_from_lengths(memory_lengths))

        mel_outputs, alignments = [], []

        while len(mel_outputs) < decoder_inputs.size(0) - 1:
            decoder_input = decoder_inputs[len(mel_outputs)]
            mel_output, attention_weights = self.decode(decoder_input)
            # mel_output : (1, B, 240)
            mel_outputs.append(mel_output)
            break
