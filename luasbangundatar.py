#Nama  : Ilham Taufiq
#Nim   : 2011102441152
#Prodi : Teknik Informatika
#kelas : AA TI Pagi

import datetime
sekarang = datetime.datetime.now()
tgl = sekarang.date()

print("\nTanggal ",tgl.day,"Bulan ",tgl.month,"Tahun ", tgl.year)

class progr:
    pembuat : '0'
    nama_prog : '0'
    
    def __init__(self, p):
        self.pembuat = p
        self.nama_prog = "Penghitungan luas bangun datar"
        
pr = progr("Ilham Taufiq")
print("\nProgram %s oleh %s\n" % (pr.nama_prog, pr.pembuat))

mydict = {
    "prog1" : "1. Hitung Luas segitiga",
    "prog2" : "2. Hitung Luas persegi",
    "prog3" : "3. Hitung luas persegi panjang",
    "prog4" : "4. Hitung luas lingkaran"
}

print(mydict["prog1"])
print(mydict["prog2"])
print(mydict["prog3"])
print(mydict["prog4"])
   
pilih = "y"
while (pilih != "n"):
    x = input("Program apa yang ingin anda gunakan? (1-4)")    
    if x == '1':
        print("\nSelamat datang di program penghitungan luas segitiga")
        alas = int(input("Masukkan nilai alas segitiga : "))
        tinggi = int(input("Masukkan nilai tinggi segitiga : "))
        luas_segitiga = 0.5 * alas * tinggi
        print("\nLuas segitiga adalah : %d" % luas_segitiga, "cm")
    
    elif x == '2':
        print("\nSelamat datang di program penghitungan luas persegi")
        sisi = int(input("Masukkan nilai sisi persegi : "))
        luas_persegi = sisi ** 2
        print("\nLuas Persegi adalah : %d" % luas_persegi, "cm")
    
    elif x == '3':
        print("\nSelamat datang di program penghitungan luas persegi panjang")
        panjang = int(input("Masukkan nilai panjang : "))
        lebar = int(input("Masukkan nilai lebar : "))
        luas_pp = panjang * lebar
        print("\nLuas persegi panjang adalah : %d" % luas_pp, "cm")

    elif x == '4':
        print("\nSelamat datang di program penghitungan luas lingkaran")
        jari = float(input('Masukkan nilai jari jari lingkaran : '))
        luas = 3.14 * (jari ** 2)
        float(luas)
        print("\nLuas lingkarang adalah : %d" % luas, "cm") 
    
    else:
        print("\nMasukkan sesuai dengan nomor program (1-4)")
    
    pilih = input("Apakah anda ingin melakukan penghitungan lagi (y/n)? ")
    
f = open("output.txt", "w")
f.write("***********File Handling************\n")
if x == '1': 
    f.write("===Luas Segitiga===\n")
    f.write("Nilai alas segitiga   : " + str(alas) + "cm \n")
    f.write("Nilai tinggi segitiga : " + str(tinggi) + "cm \n")
    f.write("Luas Segitiga         : " + str(luas_segitiga ) + "cm \n")
    
elif x == '2':
    f.write("===Luas Persegi===\n")
    f.write("Nilai sisi persegi    : " + str(sisi) + "cm \n")
    f.write("Luas Persegi          : " + str(luas_persegi) + "cm \n")
    
elif x == '3':
    f.write("===Luas Persegi Panjang===\n")
    f.write("Nilai Panjang sisi   : " + str(panjang) + "cm\n")
    f.write("Nilai lebar sisi     : " + str(lebar) + "cm\n")
    f.write("Luas persegi panjang : " + str(luas_pp) + "cm\n")
    
elif x == '4':
    f.write("===Luas Lingkaran===\n")
    f.write("Nilai jari-jari lingkaran : " + str(jari) + "cm\n")
    f.write("Luas lingkaran            : " + str(luas) + "cm\n")
    f.close()