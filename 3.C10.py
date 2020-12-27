#3
file = open('textNo2.txt', 'r')

line = file.readlines()

dic = {}
listDict = []

for x in range(len(line)) :
    y = line[x].split('|')
    y[2] = y[2].replace('\n', '')
    
    dic = {'nim' : y[0], 'nama' : y[1], 'alamat' : y[2]}
    
    listDict.append(dic)

print(listDict)
