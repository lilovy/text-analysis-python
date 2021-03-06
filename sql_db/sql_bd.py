from os import getcwd, listdir, mkdir, path
import sqlite3
import pandas as pd


def create_db(db_name: str,
              dirs: str = 'sql_db'):
    return sqlite3.connect(f"{dirs}/{db_name}.db")


db = create_db('word_rank')
c = db.cursor()


def sql_to_csv(tab: str,
               dirs: str):
    pj_dir = getcwd()
    if dirs not in listdir():
        mkdir(path.join(pj_dir, dirs)) 
    clients = pd.read_sql(f"SELECT * FROM {tab}", db)
    clients.to_csv(f"{dirs}/{tab}.csv", index=False)
    return None


def check_tb_empty(tab: str):
    pp = True
    c.execute(f"SELECT EXISTS (SELECT 1 FROM {tab});")
    if c.fetchone()[0] == 0:
        pp = False
    return pp


def create_tbl(tab: str):
    c.execute(f"""
              CREATE TABLE IF NOT EXISTS {tab} (
                word text,
                sign integer
              )
              """)
    db.commit()


def add_to_db(tab: str, text: str, param: int):
    c.execute(f"INSERT INTO {tab} ('word', 'sign') VALUES ('{text}', {param})")
    db.commit()


def update_db(tab: str, text: str, param: int):
    c.execute(f"""
              UPDATE {tab}
              SET sign = sign + {param}
              WHERE word = '{text}';
              """)
    db.commit()


def word_in_db(tab: str, text: str) -> bool:
    pp = True
    c.execute(f"""
              SELECT count (*)
              FROM {tab}
              WHERE word = '{text}';
              """)
    into = c.fetchone()[0]
    if into == 0:
        pp = False
    return pp


def tbl_exist(tab: str, tops: int):
    pp = True
    c.execute("""select * 
                 FROM ? 
                 ORDER BY sign DESC LIMIT ?;""", (tab, tops))
    into = c.fetchall()
    return into


def aggregate_db(tab: str, dicts: dict):
    for i, v in dicts.items():
        if word_in_db(tab, i):
            update_db(tab, i, v)
        else:
            add_to_db(tab, i, v)


def clear_db_tab(tab: str):
    try:
        c.execute("""DROP TABLE ?;""", (tab,))
        db.commit()
    except:
        pass


def rename_tbl(tabold: str, tabnew: str):
    c.execute(f"""ALTER TABLE {tabold}
                  RENAME TO {tabnew};""")
    db.commit()


def top_value(tab: str,
              col: str = 'sign',
              lim: str = ''):
    """ lim: 'limit {number}' """

    c.execute(f"select * from {tab} order by {col} desc {lim}")
    return c.fetchall()


def close_db():
    db.close()


def show_tbl():
    c.execute("""select * from sqlite_master
                where type = 'table'""")
    tables = [tab[1] for tab in c.fetchall()]

    return tables


def return_word(tab: str, wrd: str):
    c.execute(f"""SELECT * FROM {tab}
                  WHERE word = '{wrd}'""")
    return c.fetchall()


def word_query(querys: str) -> list:
    l = []
    for i in show_tbl():
        if check_tb_empty(i) and word_in_db(i, querys):
            l.append((i, return_word(i, querys)[0][1]))
        
    return l
