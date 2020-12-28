#3
#membuka file
file = open('textNo2.txt', 'r')

#membaca file per baris
line = file.readlines()

#membuat dictionary kosong
dic = {}
listDict = []

for x in range(len(line)) :
    #memisah data
    y = line[x].split('|')
    y[2] = y[2].replace('\n', '')
    #membuat dictionary
    dic = {'nim' : y[0], 'nama' : y[1], 'alamat' : y[2]}
    
    listDict.append(dic)

print(listDict)

#menutup file
file.close()
