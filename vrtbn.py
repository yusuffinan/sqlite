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
i = 0
while i < 10:
    rastgele()
    time.sleep(1)
    i += 1

con.close()