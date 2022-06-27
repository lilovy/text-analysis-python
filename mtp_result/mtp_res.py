from matplotlib import markers
import matplotlib.pyplot as plt


def create_plt(lst: list):
    x, y = zip(*lst)
    plt.plot(x, y, marker='o', ms=8, mec='r')

    for l, i in enumerate(lst):
        # print(i)
        plt.annotate(str(i[1]), xy=(l,i[1]), color='dodgerblue')
    # print()


def plt_inic(qry: list):
    plt.legend(qry, loc='upper left')
    plt.grid(True)


def show_plt(qry: list):
    plt.legend(qry, loc='upper left')
    plt.grid(True)
    plt.show()
