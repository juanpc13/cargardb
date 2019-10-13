
dataFile = open('prototipo2-db.sql', 'r')
txtFind = "1, -0.290838199999999991, -10.9380699999999997, -0.290838199999999991, '2019-09-29 16:43:56.049489'"
count=0


with dataFile as f:
    for line in f:
        count+=1
        if txtFind in line:
            print("Encontrado en Line: ",count)
            break

dataFile.close()