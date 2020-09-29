

class hparams:
    # Text Parameters
    cleaner_names = ['english_cleaners']

    # Audio Parameters
    # hyper parameters

    sampling_rate = 22050
    filter_length = 1024
    hop_length = filter_length // 4 # 256
    win_length = 1024
    n_mel_channels = 80
    mel_fmin =0.0
    mel_fmax = 8000.0

    # Model Parameters

    # Decoder Parameters
    n_frames_per_step = 3
