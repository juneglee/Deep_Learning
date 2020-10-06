import torch
from torch import nn

class Tacotron2Loss(nn.Module):
    def __init__(self):
        super(Tacotron2Loss, self).__init__()

    def forward(self, mel_predict, mel_target):
        mel_target.required_grad = False
        # 정답이라서 grad으로 계산하지 말아라(움지일 때마다 grad 자동으로 계산을 해놓는다)

        mel_loss = nn.MSELoss()(mel_predict, mel_target)
        return mel_loss, mel_loss.item()

