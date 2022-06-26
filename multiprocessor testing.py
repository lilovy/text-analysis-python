from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

from text_conver.load_text import del_stopwords, normalize_text

import sql_db.sql_bd as sqldb


for i in range(3):
    # sqldb.db(str(i))
    sqldb.create_db(str(i))