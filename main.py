from os import listdir, path
import re
from wordcloud_create.crt_wordcloud import wc_from_csv
from text_conver.load_text import read_json_article
from wordcloud_create.gif_create import create_gif
import sql_db.sql_bd as sdb


def main():

    """FIRST STEP: Create db of words"""
    # read_json_article(fil='lenta_news_2020_analysis')
    
    """SECOND STEP: Write db table's into csv"""
    # tabs = sdb.show_tbl()
    # for tab in tabs:
    #     if sqldb.check_tb_empty(tab):
    #         sdb.sql_to_csv(tab)

    """THIRD STEP: Create WordCloud with csv"""
    # tath = (path.dirname(__file__))
    # tab = 'words_csv'
    # dirs = listdir(f"{tath}/{tab}")
    # for file in dirs:
    #     wc_from_csv(file, 'words_csv')

    """FOURTH STEP: Create gif"""
    # create_gif('dynamic', fold='picture')

    # print(sdb.return_word('month_05', 'коронавирус')[0][1])


if __name__ == '__main__':
    main()
