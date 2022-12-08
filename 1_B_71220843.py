print("SELAMAT DATANG DI PENCARIAN PEMBUAT PIRAMIDA BERLUBANG")
q =int(input("Masukkan Angka: "))

print (' '*(q-1),'*')
for p in range ((q-1),1,-1):

    print(' '*(p-1), '**')   

print('**'*q)
