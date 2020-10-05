import torch
from torch import nn
from model.encoder import Encoder
from model.decoder import Decoder
# from model.modules import Postnet
from hparams import hparams as hps
from math import sqrt


class Tacotron2(nn.Module):
    def __init__(self):
        super(Tacotron2, self).__init__()

        self.embedding = nn.Embedding(hps.n_symbols, hps.character_embedding_dim)

        self.encoder = Encoder()
        self.decoder = Decoder()

    def forward(self, inputs):
        text_inputs, input_lengths, mel_targets = inputs
        print('input_text_size : ', text_inputs.size())
        character_embedding = self.embedding(text_inputs)
        # (Batch, seq_len, 512)
        # (Batch, 512, seq_len) transpose로 들어가야 한다.
        print('character_embedding_size : ', character_embedding.size())
        character_embedding = character_embedding.transpose(1, 2) # 행과열을 바꿔줌
        print('character_embedding_size : ', character_embedding.size())

        encoder_outputs = self.encoder(character_embedding, input_lengths)
        print('encoder output size : ', encoder_outputs.size())

        self.decoder(encoder_outputs, mel_targets, input_lengths)


if __name__ == '__main__':
    from feeder.speech_dataset import SpeechDataset, SpeechCollate
    dataset = SpeechDataset('../data/lj')
    collate_fn = SpeechCollate()

    from torch.utils.data import DataLoader

    dataloader = DataLoader(dataset, num_workers=0, shuffle=True,
                            batch_size=5, drop_last=True,
                            collate_fn=collate_fn)

    model = Tacotron2()

    for batch in dataloader:
        mel_padded, output_lengths, text_padded, input_lengths = batch
        model((text_padded.long(), input_lengths.long(), mel_padded.float()))
        break





    # text = "hello tacotron"
    #
    # from text import text_to_sequence
    # t2s = text_to_sequence(text, ['english_cleaners'])
    # t2s = torch.IntTensor(t2s)
    # t2s = t2s.unsqueeze(0)
    #
    # model = Tacotron2()
    # model.eval() # false
    # print(model.training)
    # model.train() # true
    # print(model.training)
    # model(t2s.long()) # embedding은 long type으로만 받는다.