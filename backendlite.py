# -*- coding: utf-8 -*-

import sqlite3

#VARIABLES ZONE
server = 'tcp:35.224.23.215,1433'
database = 'books'
username = 'books'
psw = 'Book2019'

def connect():
    conn = sqlite3.connect("books.db")
    return conn

def connect1():
    conn = connect()
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY,   \
    title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()
    
def insert(title,author,year,isbn):
    conn=connect()
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",                   \
                (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR  \
                isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete (id):
    conn=connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update (id, title,author,year,isbn):
    conn=connect()
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?" \
                ,(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("Letter","Jhon",1938,12345)
#delete(2)
#update(7,'Lett','Jh',1900,20000)
#print(view())
#print("---")
#print(search("Letter"))