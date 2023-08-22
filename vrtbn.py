import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler1.db")
cursor = con.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT, anahtark TEXT, deger REAL)")

def rastgele():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtark = "Pythpon Sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman, tarih, anahtark, deger) VALUES(?,?,?,?)", (zaman, tarih, anahtark, deger))
    con.commit()
tablo()
#i = 0
#while i < 10:
#    rastgele()
#    time.sleep(1)
#    i += 1

def degeral():
    cursor.execute(" SELECT * FROM Tablo1 WHERE deger =4.0 ")
    data = cursor.fetchall()
    for i in data:
        print(i)
degeral()

def guncelle():
    cursor.execute(" SELECT * FROM Tablo1 ")
    print("öncesi---------------")
    data = cursor.fetchall()
    for i in data:
        print(i)
    cursor.execute("UPDATE Tablo1 SET deger = 99 WHERE deger = 4")
    cursor.execute(" SELECT * FROM Tablo1 ")
    print("sonrası---------------")
    data = cursor.fetchall()
    for i in data:
        print(i)

guncelle()

def sil():
    cursor.execute("DELETE FROM Tablo1 WHERE deger = 5 ")
    cursor.execute("SELECT * FROM Tablo1")
    print("silindi")
    data = cursor.fetchall()
    for i in data:
        print(i)
    con.commit()

sil()    
con.close()