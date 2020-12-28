#7
def decrypt(teks, n):
    
    listTeks = list(teks)

    for x in range(len(listTeks)):
        
        if(listTeks[x] != ' '):

            if(ord(listTeks[x]) - n >= 65):
                asciiCode = ord(listTeks[x])
                didecrypt = asciiCode - n
                listTeks[x] = chr(didecrypt)

            else :
                asciiCode = ord(listTeks[x])
                didecrypt = (asciiCode + 26) - n
                listTeks[x] = chr(didecrypt)

        else :  
            continue

    hasil = ''.join(listTeks)

    return hasil


try :
    
    teks = input('Inputkan teks yang ingin dienkripsi :')
    n = int(input('Berapa jumlah geseran pada enkripsi :'))

    hasil = decrypt(teks, n)
    print('\nHasil enkripsi dari teks {0} yaitu : {1}'.format(teks, hasil))

except ValueError :
    print('Inputkan khusus bilangan bulat')
