from os import listdir, path
import re
import wordcloud_create.crt_wordcloud as wc
from text_conver.load_text import read_json_article
from wordcloud_create.gif_create import create_gif
import sql_db.sql_bd as sdb
from mtp_result.mtp_res import create_plt, show_plt


def create_db(fil: str = 'lenta_news_2020_analysis'):
    read_json_article(fil)


def db_to_csv(dirs: str = 'words_csv'):
    tabs = sdb.show_tbl()
    for tab in tabs:
        if sdb.check_tb_empty(tab):
            sdb.sql_to_csv(tab, dirs)


def wc_with_csv(tab: str = 'words_csv'):
    tath = (path.dirname(__file__))
    dirs = listdir(f"{tath}/{tab}")
    for file in dirs:
        wc.wc_from_csv(file, tab)


def gif_create(name: str = 'dynamic', direct: str = 'picture'):
    create_gif(name, direct)


def show_word(args: list):
    l = []
    for q in args:
        lst = sdb.word_query(q)
        if len(lst) != 0:
            l.append(q)
            create_plt(lst)
    show_plt(l)


def main():

    """FIRST STEP: Create db of words"""
    
    # create_db()
    
    """SECOND STEP: Write db table's into csv"""

    # db_to_csv()

    """THIRD STEP: Create WordCloud with csv"""
    
    # wc_with_csv()

    """FOURTH STEP: Create gif"""

    # gif_create()


    """SHOW WORD'S PLOT"""

    show_word(["кот", "сидеть", "война", "хлопок"])



if __name__ == '__main__':
    main()
