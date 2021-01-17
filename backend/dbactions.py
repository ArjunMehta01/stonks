#import sqlite3
#
#def insert_entry(sub_id,title,body,url,author,score, upvoteratio, created, numComms,permalink, flair, awards):
#    conn = sqlite3.connect('stonk.db')
#    c = conn.cursor()
#    inputs = (sub_id,title,body,url,author,score, upvoteratio, created, numComms,permalink, flair, awards)
#    c.execute("INSERT INTO posts VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", inputs)
#    conn.commit()
#    conn.close()
#


import sqlite3
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import STOPWORDS

my_stop_words = STOPWORDS.union(set(['I','The','If','But','This','like','going']))
word_list = []
d = {}

conn = sqlite3.connect('stonks.db')
c = conn.cursor()
c.execute("select pbody from posts where  pbody <> '[removed]'")
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
    d[word] = d.get(word,0)+1

word_freq = []
for key, value in d.items():
    if value == 1:
        pass
    else:
        word_freq.append((value,key))

word_freq.sort(reverse=True)
print(word_freq)