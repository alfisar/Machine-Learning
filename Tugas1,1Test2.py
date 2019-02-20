import numpy
import csv
import math

# Mendapatkan probabilitas dari kelas
def probclass(lis2):
    prob50,probkrng50,lebih50,krngsma50,hasil = 0.0,0.0,0.0,0.0,0.0
    for row in lis2:
        if(row[8] == '>50K'):
            lebih50 += 1
        else :
            krngsma50 += 1
    hasil = lebih50 + krngsma50
    prob50 = lebih50 / hasil
    probkrng50 = krngsma50 / hasil
    return prob50,probkrng50,lebih50,krngsma50 

# Mendapatkan probabilitas atribut terhadap kelas
def xterhadapc(lis4,lis2):
    for ro in lis4:
        temp50,tempkrng = 0.0,0.0
        for row in lis2 :
            for i in range(1,8):
                if(ro == row[i]) and (row[8] == '>50K'):
                    temp50 += 1
                elif (ro == row[i]) and (row[8] == '<=50K'):
                    tempkrng += 1
        temp50 = temp50 / lbh50
        tempkrng = tempkrng / krng50 
        lis5.append((ro,temp50,tempkrng))
        i+=1
    return lis5

# mendapatkan semua atribut
def atribut(lis2):
    for row in lis2 :
        for i in range(1,8):
            temp = False
            if(lis4 == []):
                lis4.append(row[i])
            else:
                for j in lis4:
                    if (j == row[i]):
                        temp = True
                if (temp != True):
                    lis4.append(row[i])
    return lis4
# mendapatkan probabilitas dari atribut
def probatribut(roww,i,lis2):
    temp,j = 0.0,0
    for row in lis2:
        if(row[i] == roww[i]):
            temp += 1
        j+=1
    temp = temp / j
    return temp

# Mendapatkan hasil akhir masuk ke kelas >50K atau <=50K
def penentuan(l50,k50,hasilpem,lis3):
    l50 = (l50 * prob50) / hasilpem
    k50 = (k50 * probkrng50) / hasilpem
    if (l50 >= k50) :
        lis3.append('>50K')
    else:
        lis3.append('<=50K')
    return lis3

f = open("TrainsetTugas1ML.csv","r")
reader = csv.reader(f)
next(reader)

g = open("TestsetTugas1ML.csv","r")
reader1= csv.reader(g)
next(reader1)

lis1,lis2,lis3,lis4,lis5 = [],[],[],[],[]
temp = 0
for d in reader :
    lis2.append((d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]))

for d in reader1 :
    lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))


prob50,probkrng50,lbh50,krng50 = probclass(lis2)
lis4 = atribut(lis2)
lis5 = xterhadapc(lis4,lis2)

# print(lis5)

j = 1
for roww in lis1:
    l50,k50,hasilpem = 1.0,1.0,1
    for i in range(1,8):
        for row in lis5 :
           if row[0] == roww[i]:
               l50 = l50 * row[1]
               k50 = k50 * row[2]
        pem = probatribut(roww,i,lis2)
        hasilpem = hasilpem * pem
    lis3 = penentuan(l50,k50,hasilpem,lis3)

print(lis3)
