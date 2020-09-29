import torch
import numpy as np
from scipy.signal import get_window
import librosa.util as librasa_util
import librosa
from hparams import hparams as hps


def load_wav_torch(wav_path):
    wav, sr = librosa.core.load(wav_path, sr=hps.sampling_rate)
    wav = wav.astype(np.float32)
    # normalization
    wav = wav / np.max(np.abs(wav))
    wav = torch.from_numpy(wav).float()
    return wav

def dynamic_range_compression(mel_sepctrogram, C=1, min_clip_val = 1e-5):
    # audio processing
    # -1 ~ 1
    # print('input', mel_sepctrogram.size(), torch.min(mel_sepctrogram))

    clamp = torch.clamp(mel_sepctrogram, min = min_clip_val)
    # print('clamp', clamp.size(), torch.min(clamp))

    clamp_factor = clamp * C
    # print('clamp_factor', clamp_factor.size(), torch.min(clamp_factor))

    log_mel_spectrogram = torch.log(clamp_factor)
    # print('log_mel_spectrogram', log_mel_spectrogram.size(), torch.min(log_mel_spectrogram))

    return log_mel_spectrogram
