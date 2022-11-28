from Summary import Summary
from mecab import MeCab

class Keyword:
    mecab = MeCab()
    def __new__(cls, sent, **kwargs):
        summary = Summary(sent)
        return ' '.join(list(set(cls.mecab.nouns(summary))))