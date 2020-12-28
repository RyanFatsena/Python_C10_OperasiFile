#2
#membuka file
file = open('textNo2.txt','a')

i = True
while ( i == True) :
    nim = input('Masukkan NIM      : ')
    namaMhs = input('Masukkan Nama Mhs : ')
    alamat = input('Masukkan Alamat   : ')
   
    file.write(nim + '|' + namaMhs + '|' + alamat + '\n')  
    ulangi = input('Ulangi input lagi (y/n) : \n')
    
    if (ulangi.lower() == 'y') :
        i = True
    elif (ulangi.lower() == 'n'):
        i = False
    else :
        print ('Inputan yang dimasukkan invalid')
        continue
#menutup file
file.close()
