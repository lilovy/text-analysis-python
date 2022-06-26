import csv
from os import listdir, mkdir, path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('sql_db\month_01.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    d = {}
    for k,v in reader:
        d[k] = int(v)
    # data = list(reader)[1:]
    # print(data)
    # lst = '\t'.join([i[0] for i in data])


# reader = csv.reader(open('namesDFtoCSV', 'r',newline='\n'))
# d = {}
# for k,v in reader:
#     d[k] = int(v)

#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wordcloud = WordCloud(width=900,height=500, 
                      max_words=1628,relative_scaling=1,
                      normalize_plurals=False).generate_from_frequencies(d)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

