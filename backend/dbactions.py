import sqlite3
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import STOPWORDS
import pandas as pd

my_stop_words = STOPWORDS.union(set(['I','The','If','But','This','like','going']))
word_list = []
flair_list = ['Loss','Gain']
d = {}

def freq_for_all():
    conn = sqlite3.connect('stonks.db')
    c = conn.cursor()
    c.execute("select text from posts where  text <> '[removed]'")
    total = c.fetchall()
    for i in total:
        for x in i:
            filtered = remove_stopwords(x)
            split = filtered.split()
            for z in split:
                if z in my_stop_words:
                    pass
                else:
                    word_list.append(z)

    conn.commit()
    conn.close()

    for word in word_list:
        d[word] = d.get(word, 0) + 1

    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))

    word_freq.sort()
    print(word)

def flair_search():
    flair_list = ['Loss', 'Gain']
    conn = sqlite3.connect('stonks.db')
    c = conn.cursor()
    c.execute("select * from posts where Flair == 'Loss' or Flair == 'Gain';")
    total = c.fetchall()
    df = pd.DataFrame(total, columns = ['PostID','Title','text','Url','Author','Score','PublishDate','TotalNo.ofComments','Permalink','Flair','awards'])

    df.to_csv('loss_gain_only.csv')


def search(stock):

    for key, value in d.items():
        if key == stock:
            print(key,value)
def main():
    #freq_for_all()
    #search('Tesla')
    flair_search()

main()
