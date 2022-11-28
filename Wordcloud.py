from wordcloud import WordCloud
from collections import Counter
from mecab import MeCab
from base64 import b64encode

class Wordcloud:
    wc = WordCloud(font_path='malgun', width=326, height=178, scale=2.0, max_font_size=200, background_color="rgba(255, 255, 255, 0)", mode="RGBA")
    mecab = MeCab('C:\mecab\mecab-ko-dic')
    def __new__(cls, text):
        text = cls.mecab.nouns(text)
        cls.wc.generate_from_frequencies(Counter(text))
        cls.wc.to_file('tmp_wordcloud.png')
        return b64encode(open("tmp_wordcloud.png", "rb").read())
