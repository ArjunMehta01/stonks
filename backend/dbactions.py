import sqlite3

def insert_entry(sub_id,title,body,url,author,score, upvoteratio, created, numComms,permalink, flair, awards):
    conn = sqlite3.connect('stonk.db')
    c = conn.cursor()
    inputs = (sub_id,title,body,url,author,score, upvoteratio, created, numComms,permalink, flair, awards)
    c.execute("INSERT INTO posts VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", inputs)
    conn.commit()
    conn.close()

def extract(sub_id)