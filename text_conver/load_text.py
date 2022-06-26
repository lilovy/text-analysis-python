import sys
# sys.path.insert(1, "/text-analysis-python/sql_db")
import sql_bd as sqldb
import os
import json
# from matplotlib.pyplot import text
import pymorphy2
import nltk
from nltk.corpus import stopwords
import string
from collections import Counter
# import sql_db.sql_bd as sqldb
print(sys.path)

def remove_chars_from_text(text: str, chars: str) -> str:
    return "".join([ch for ch in text if ch not in chars])


def del_stopwords(tx: str) -> list:
    nltk.download('stopwords')
    text = nltk.word_tokenize(tx)
    ru_stopwords = set(stopwords.words("russian"))
    new_stopwords = ['год', "это", "свой", "тот", "который", 'каждый', 
                     "такой", "быть", "мочь", 'новый', "весь", 
                     "однако", "стать", "весь", 'также', "слово",
                     "ещё", "самый", 'изз', "всё", "время", "человек",
                     'страна', "январь", "февраль", "март", "апрель",
                     "май", 'заявить']
    ru_stopwords = ru_stopwords.union(new_stopwords)
    filtered_words = [word for word in text if word not in ru_stopwords]

    return filtered_words



def normalize_text(text: str) -> str:
    morph = pymorphy2.MorphAnalyzer()
    spec_chars = string.punctuation + '\n\xa0«»\t—…0123456789'
    new_text = remove_chars_from_text(text, spec_chars)
    text = new_text.lower().split()
    texts = [morph.parse(i)[0].normal_form for i in text]

    return ' '.join(texts)


def completely(lst: list) -> str:
    z = ''
    for i in lst:
        z += ' '.join(del_stopwords(normalize_text(i)))

    return z


def read_json_article(fil: str) -> list:
    """
    Create sqlite db with words from uploaded texts.

    fil 
     upload directory
    
    
    """ 
    files = sorted(os.listdir(fil), key=lambda fn:os.path.getctime(os.path.join(fil, fn)))
    # lst = []

    for i, dates in enumerate(files):
        month = dates[5:7]
        tab = f'month_{month}'
        if dates[8:10] == '01':
            sqldb.clear_db_tab(tab)
        sqldb.create_tbl(tab)
        news = f'{fil}/{dates}'

        for l, article in enumerate(os.listdir(news)):

            drct = f'{news}/{article}'
            with open(drct, encoding='utf-8') as f:
                data = json.load(f)
                artcl = data.get('text')
                # lst.append(artcl)
                sqldb.aggregate_db(tab, dict(Counter(del_stopwords(normalize_text(artcl)))))
        print(i, 'i')

    sqldb.close_db()
