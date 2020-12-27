#1
file = open('textNo1.txt', 'r')

textNo1 = file.readlines()

genap = []
ganjil = []

for x in range(len(textNo1)) :
    if('\n' in textNo1[x] == True) :
        textNo1[x].replace('\n', '')

        if(int(textNo1[x])%2 == 0) :
            genap.append(textNo1[x])
        else :
            ganjil.append(textNo1[x])

    else :
        if(int(textNo1[x])%2 == 0) :
            genap.append(textNo1[x])
        else :
            ganjil.append(textNo1[x])

print('Banyaknya bilangan genap : {0}'.format(len(genap)))
print('Banyaknya bilangan ganjil : {0}'.format(len(ganjil)))
