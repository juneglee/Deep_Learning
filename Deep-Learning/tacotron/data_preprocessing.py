import torch
import os
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from audio.stft import TacotronSTFT
from audio.utils import load_wav_torch
from hparams import hparams as hps
from tqdm import tqdm


def preprocessing(dataset_dir, wav_index=0, transcript_index=2, wav_dir= 'wavs',
                  sperator='|', file_extention = 'wav'):
    # file_extention : 호환성을 위하 미리 정해둠
    # wav_index : metadata의 index 0
    # transcript_index : metadata의 index 2
    futures = []

    max_workers = multiprocessing.cpu_count() // 2 # 4
    executor = ProcessPoolExecutor(max_workers=max_workers)
    # max_workers 몇개로 돌릴지 정한다(cpu의 코어보다 높으면 의미없다)

    metadata_path = os.path.join(dataset_dir, 'metadata.csv')
    metadata = load_metadata(metadata_path, wav_index, transcript_index, wav_dir)

    traindata_dir = os.path.join(dataset_dir, 'traindata_%d' % hps.sampling_rate )
    mel_dir = os.path.join(traindata_dir, 'mels')

    os.makedirs(mel_dir, exist_ok=True)

    results =[]
    index = 0
    for data in tqdm(metadata):
        wav_path, transcript = data
        # result = processing(mel_dir, index, wav_path, transcript)
        task = partial(processing, mel_dir, index, wav_path, transcript)
        # processing 함수로 사용하지 않고 변수처럼 사용한다.
        # results.append(result)
        futures.append(executor.submit(task))
        index += 1

    results = [future.result() for future in tqdm(futures)] # 순서에는 상광없이 출력한다. 그래서 index를 이용하여 정렬
    results = sorted(results, key=lambda result:result[0])
    write_train_metadata(traindata_dir, results)

def write_train_metadata(date_dir, metadata):
    write_filename = 'train metadata.csv'
    write_filename = os.path.join(date_dir,write_filename)

    # w와 a의 차이는 기존의 밑에 작성 a
    with open(write_filename, 'w', encoding='utf-8') as f:
        for data in metadata:
            line = "|".join(list(data[1:]))
            f.write(line + '\n')

def processing(mel_dir, index, wav_path, transcript):
    stft = TacotronSTFT()
    wav = load_wav_torch(wav_path)

    # (Y) -> (B, Y)
    wav = wav.unsqueeze(0)
    wav = torch.autograd.Variable(wav, requires_grad=False) # requires_grad 미분계산을 하지 않도록 선언 back

    mel_spectrogram = stft.mel_spectrogram(wav)
    # mel : (B, N, F) 배치는 어짜피 1이기 때문에 줄여준다
    # mel : (B, N, F) -> (N, F)
    mel_spectrogram = mel_spectrogram.squeeze(0)

    mel_filename = 'mel_spec_%05d.pt' % index
    mel_filepath = os.path.join(mel_dir, mel_filename)

    torch.save(mel_spectrogram, mel_filepath)

    return index, mel_filename, transcript

def load_metadata(path, findex, tindex, wav_dir):
    # f = open(path, 'r', encoding='utf-8')
    # f.readline()
    # f.close()
    metadata = []
    base_dir = os.path.dirname(path)
    with open(path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            items = line.split('|')
            # [filename, script, script]
            wav_filename = items[findex]
            wav_path = os.path.join(base_dir, wav_dir, '%s.wav' % wav_filename)
            transcript = items[tindex]
            metadata.append([wav_path, transcript])

    return metadata


if __name__ == '__main__':
    ljspeech_dataset = './data/lj'
    preprocessing(ljspeech_dataset)
    # print(multiprocessing.cpu_count()) # 8