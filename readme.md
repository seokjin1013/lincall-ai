## USE_model

download model at https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3

tar -xvzf universal-sentence-encoder-multilingual-large_3.tar.gz

## STT_model.pt

https://github.com/sooftware/kospeech/issues/154

## mecab-ko on windows

https://uwgdqo.tistory.com/363

https://github.com/Pusnow/mecab-ko-msvc/releases/tag/release-0.9.2-msvc-3
https://github.com/Pusnow/mecab-ko-dic-msvc/releases/tag/mecab-ko-dic-2.1.1-20180720-msvc-2

### mecab_python-0.996_ko_0.9.2_msvc-cp37-cp37m-win_amd64.whl

https://github.com/Pusnow/mecab-python-msvc/releases/tag/mecab_python-0.996_ko_0.9.2_msvc-3

## installation

pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

.venv\lib\site-packages\pororo\models\brainbert\BrainRoBERTa.py
add following code at __init__ function

    from dataclasses import dataclass
    @dataclass
    class Args:
        task = "sentence_prediction"
        regression_target = False
    self.args = Args()