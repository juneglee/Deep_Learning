from torch import nn
from torch.nn import functional as F
from hparams import hparams as hps
from model.layers import ConvNorm

class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()

        # self.conv_1d_first = nn.Conv1d(512, 512, kernel_size=0, stride=0, padding=0,
        #                                dilation=1)
        # self.conv_1d_second =
        # self.conv_1d_third =

        convolutions = []
        for _ in range(hps.encoder_n_convolutions):
            conv_layer = nn.Sequential(
                ConvNorm(hps.character_embedding_dim,
                         hps.encoder_embedding_dim,
                         kernel_size=hps.encoder_kernel_size,
                         stride=1, padding=int((hps.encoder_kernel_size - 1) / 2),
                         dilation=1),
                nn.BatchNorm1d(hps.encoder_embedding_dim))
            convolutions.append(conv_layer)

        self.convolutions = nn.ModuleList(convolutions)

        self.lstm = nn.LSTM(hps.encoder_embedding_dim,
                            int(hps.encoder_embedding_dim / 2), num_layers=1,
                            batch_first= True, bidirectional= True)

    def forward(self, inputs, input_lengths):
        x = inputs
        # input : char embedding
        # (conv1d -> batchnorm1d -> relu -> drop out) * 3
        for conv in self.convolutions:
            x = F.dropout(F.relu(conv(x)), hps.encoder_dropout_p, self.training)
            # print('encoder conv : ', x.size())

        x = x.transpose(1, 2)
        # print('encoder lstm input : ', x.size())

        input_lengths = input_lengths.cpu().numpy()
        x = nn.utils.rnn.pack_padded_sequence(x, input_lengths, batch_first=True)

        self.lstm.flatten_parameters()
        x, _ = self.lstm(x)

        x, _ = nn.utils.rnn.pad_packed_sequence(x, batch_first=True)

        # print('lstm output : ', x.size())

        return x
