from os import getcwd, path, mkdir, listdir
from wordcloud import WordCloud
from collections import defaultdict
import csv
import matplotlib.pyplot as plt


def create_wordcloud(text: str, 
                     tab: int,
                     direct: str = 'picture'): 
    if direct not in listdir():
        mkdir(path.join(getcwd(), direct)) 
 
    wc = WordCloud(width=900,height=500, 
                   max_words=1628,relative_scaling=1,
                   normalize_plurals=False)
    wc.generate(text)
    wc.to_file(f"{direct}\{tab}.png")


def wc_from_csv(tab: str,
                dirs: str,
                direct: str = 'picture'):

    if direct not in listdir():
        mkdir(path.join(getcwd(), direct)) 

    with open(f"{getcwd()}\{dirs}\{tab}", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        d = {}
        for k,v in reader:
            d[k] = int(v)

    wc = WordCloud(width=900,height=500, 
                   max_words=1628,relative_scaling=1,
                   normalize_plurals=False).generate_from_frequencies(d)

    tab = tab.replace('.csv', '')
    wc.to_file(f"{direct}/{tab}.png")
