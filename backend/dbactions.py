import sqlite3
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import STOPWORDS
import pandas as pd
import csv

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
    conn = sqlite3.connect('stonks.db')
    c = conn.cursor()
    c.execute("select * from posts where Flair == 'Loss' or Flair == 'Gain';")
    total = c.fetchall()
    df = pd.DataFrame(total, columns = ['PostID','Title','text','Url','Author','Score','PublishDate','TotalNo.ofComments','Permalink','Flair','awards'])

    df.to_csv('loss_gain_only.csv')
    conn.commit()
    conn.close()


def search(stock):

    for key, value in d.items():
        if key == stock:
            print(key,value)

def flair_sort():
    with open('loss_gain_only.csv', 'r') as infile, open('reordered.csv', 'a') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Flair', 'Title', 'text', 'Url', 'Author','Score','PublishDate','TotalNo.ofComments','Permalink','Flair','awards','PostID','']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            for i in row:
                if i == 'Flair':
                    if row[i] == 'Loss':
                        row[i] = 1
                    else:
                        row[i] = 2
            writer.writerow(row)

def flair_change():
    # making data frame from the csv file
    dataframe = pd.read_csv("reordered.csv")

    # using the replace() method
    dataframe.replace(to_replace="Loss",
                      value="1",
                      inplace=True)
    dataframe.replace(to_replace="Gain",
                      value="2",
                      inplace=True)

    # writing  the dataframe to another csv file
    dataframe.to_csv('reordered.csv',
                     index=False)
def main():
    #freq_for_all()
    #search('Tesla')
    #flair_search()
    #flair_sort()
    flair_change()

main()
