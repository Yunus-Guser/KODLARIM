print('''
list işlem listesi

1. Toplama İşlemi
2. Çikarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
''')

while True:
    işlem = input("İşlem Seçiniz (çikiş için q'ya basiniz): ")
    if işlem == 'q':
        print("Çikiliyor...")
        break
    elif işlem == '1':
        print("------Toplama İşlemi------")
        sayi1 =int(input("1. Sayiyi Giriniz: "))
        sayi2 =int(input("2. Sayiyi Giriniz: "))
        print ("{}+{}={}".format(sayi1,sayi2,sayi1+sayi2))
    elif işlem == '2':
        print("------Çıkarma İşlemi------")
        sayi1 =float(input("1. Sayiyi Giriniz: "))
        sayi2 =float(input("2. Sayiyi Giriniz: "))
        print ("{}-{}={}".format(sayi1,sayi2,sayi1-sayi2))
    elif işlem == '3':
        print("------Çarpma İşlemi------")
        sayi1 =float(input("1. Sayiyi Giriniz: "))
        sayi2 =float(input("2. Sayiyi Giriniz: "))
        print ("{}*{}={}".format(sayi1,sayi2,sayi1*sayi2))
    elif işlem == '4':
        print("------Bölme İşlemi------")
        try:
            sayi1 =int(input("1. Sayiyi Giriniz: "))
            sayi2 =int(input("2. Sayiyi Giriniz: "))
            print ("{}/{}={}".format(sayi1,sayi2,sayi1/sayi2))
        except ZeroDivisionError:
            print("Bir Sayi Sifira Böünemez")
    else:
        print("Geçersiz İşlem")