import sqlite3

con = sqlite3.connect("dersler1.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, soyad TEXT, numara INT, notum INT)")

def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('yusuf', 'inan', 126, 75)")
    con.commit()
    con.close()
tablo_olustur()
degerekle()