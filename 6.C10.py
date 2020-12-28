#6
def encrypt(teks, n):
    
    listTeks = list(teks)

    for x in range(len(listTeks)):
        
        if(listTeks[x] != ' '):
            
            if(ord(listTeks[x]) + n < 90):
                asciiCode = ord(listTeks[x])
                dienkripsi = asciiCode + n
                listTeks[x] = chr(dienkripsi)

            else :
                asciiCode = ord(listTeks[x])
                dienkripsi = (asciiCode + n) - 26
                listTeks[x] = chr(dienkripsi)

        else :  
            continue

    hasil = ''.join(listTeks)

    return hasil


try :
    
    teks = input('Inputkan teks yang ingin dienkripsi :')
    n = int(input('Berapa jumlah geseran enkripsi :'))

    hasil = encrypt(teks, n)
    print('\nHasil enkripsi dari teks {0} yaitu : {1}'.format(teks, hasil))

except ValueError :
    print('Inputkan khusus bilangan bulat')
