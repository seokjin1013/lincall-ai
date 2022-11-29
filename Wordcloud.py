from wordcloud import WordCloud
from collections import Counter
from mecab import MeCab
from base64 import b64encode
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np

class Wordcloud:
    wc = {}
    wc['base'] = WordCloud(font_path='malgun', width=326, height=178, scale=2.0, max_font_size=50, background_color="rgba(255, 255, 255, 0)", mode="RGBA")
    wc['dark'] = WordCloud(font_path='malgun', width=326, height=178, scale=2.0, max_font_size=50, background_color="rgba(255, 255, 255, 0)", mode="RGBA", colormap=ListedColormap(mpl.colormaps['gray'](np.linspace(0, 0.5, 128))), prefer_horizontal=1)
    wc['tab20c'] = WordCloud(font_path='malgun', width=326, height=178, scale=2.0, max_font_size=50, background_color="rgba(255, 255, 255, 0)", mode="RGBA", colormap=mpl.colormaps['tab20c'])
    mecab = MeCab('C:\mecab\mecab-ko-dic')
    def __new__(cls, text, theme):
        text = cls.mecab.nouns(text)
        cls.wc[theme].generate_from_frequencies(Counter(text) or Counter(' '))
        cls.wc[theme].to_file('tmp_wordcloud.png')
        return b64encode(open("tmp_wordcloud.png", "rb").read())
