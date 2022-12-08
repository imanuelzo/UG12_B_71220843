print ("~~~ Selamat Datang di Kalkulator Serderhana ~~~")
msk = int(input("Masukkan operator matematika yang ingin Anda hitung: "))
x = int(input("Mau Penjumlahan berapa: "))
y = int(input("Print berapa banyak:" ))
def Add():
    tambah = x + y
    print (x, "+", y, "=", tambah)
def subtract():
    kurangi = x - y
    print (x, "-", y, "=", kurangi)
def multiply():
    kali = x * y
    print (x, "*", y, "=", kali)
def divide():
    per = x / y
    print (x, "/", y, "=", per)