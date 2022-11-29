from Summary import Summary
from mecab import MeCab

class Keyword:
    mecab = MeCab()
    def __new__(cls, sent, **kwargs):
        summary = Summary(sent)
        summary_words = set(cls.mecab.common_nouns(summary))
        original_words = set(cls.mecab.morphs(sent))
        return ' '.join(summary_words & original_words)