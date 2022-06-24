import os
import json
import pymorphy2
import nltk
from nltk.corpus import stopwords
import string


# nltk.download('stopwords')

fil = 'lenta_news_2020_analysis'
files = sorted(os.listdir(fil), key=lambda fn:os.path.getctime(os.path.join(fil, fn)))


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])



def del_stopwords(tx: str) -> list:
    spec_chars = string.punctuation + '\n\xa0«»\t—…'
    tx = tx.lower()
    ru_stopwords = stopwords.words("russian")
    new_text = remove_chars_from_text(tx, spec_chars)
    text_tokens = nltk.word_tokenize(new_text)
    text = nltk.Text(text_tokens)
    filtered_words = [word for word in text if word not in ru_stopwords]


    return filtered_words


def normalize_text(text: list) -> list:
    morph = pymorphy2.MorphAnalyzer()
    texts = [morph.parse(i)[0].normal_form for i in text]

    return texts


def read_json_article() -> list:
    lst = []
    for dates in files:
        news = f'{fil}/{dates}'

        for article in os.listdir(news):

            drct = f'{news}/{article}'
            with open(drct, encoding='utf-8') as f:
                data = json.load(f)
                artcl = data.get('text')
                # clear_text = del_stopwords(artcl)

                lst.append(artcl)

            break

        break
    return lst


# lst = read_json_article()
# for l in lst:
#     z = del_stopwords(l)
#     z = normalize_text(z)
#     print(z)

# morph = pymorphy2.MorphAnalyzer()
# for i in ('собаки', 'бегал'):
#     z = morph.parse(i)[0].normal_form
#     print(z)