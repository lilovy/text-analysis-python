from load_text import *


def main():
    # daynews = read_json_article()
    lst = read_json_article()
    for l in lst:
        z = del_stopwords(l)
        z = normalize_text(z)
        print(z)
    # print(len(daynews))
    # print('hi')


if __name__ == '__main__':
    main()
