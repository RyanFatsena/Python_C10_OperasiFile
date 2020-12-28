#4
mencariNim = input('Inputkan NIM yang dicari :')
#membuka file
file = open('textNo2.txt', 'r')

y = file.readlines()

for x in range(len(y)) :
    
    if(mencariNim in y[x]) :
        status = 'ada'
        break

    else :
        status = 'tidak ada'
        continue

if(status == 'ada') :
    
        z = y[x].split('|')
        
        print('\nData Mahasiswa')
        print('NIM    :', z[0])
        print('Nama   :', z[1])
        print('Alamat :', z[2])

else :
    print('Data mahasiswa tidak ditemukan')
    
#menutup file
file.close()
