import torch
import torchaudio
import numpy as np
import librosa
from kospeech.vocabs.ksponspeech import KsponSpeechVocabulary

class STT:
    device = "cpu"
    model_path = "./STT_model.pt"
    vocab = KsponSpeechVocabulary('./aihub_character_vocabs.csv')
    model = torch.load(model_path, map_location=lambda storage, _: storage).module.to(device)

    def parse(signal):
        feature = torchaudio.compliance.kaldi.fbank(
            waveform=torch.tensor(signal).unsqueeze(0),
            num_mel_bins=80,
            frame_length=20,
            frame_shift=10,
            window_type='hamming'
        ).transpose(0, 1).numpy()
        feature -= feature.mean()
        feature /= np.std(feature)
        return torch.FloatTensor(feature).transpose(0, 1)

    def revise(sentence):
        words = sentence.split()
        result = []
        for word in words:
            tmp = word[0] + ''.join([word[i] for i in range(1, len(word)) if word[i] != word[i - 1]])
            if tmp == '스로':
                tmp = '스스로'
            result.append(tmp)
        return ' '.join(result)

    def __new__(cls, path):
        wav_data, sr = librosa.load(path, sr=16000)
        feature = cls.parse(wav_data)
        input_length = torch.LongTensor([len(feature)])

        y_hats = cls.model.recognize(feature.unsqueeze(0), input_length)
        sentence = cls.vocab.label_to_string(y_hats.cpu().detach().numpy())[0]
        return cls.revise(sentence)