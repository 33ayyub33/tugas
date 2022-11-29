#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10


Ninja = eval(input())
mNinja = []

def isempty(a):
    return a == []

def besar(ma):
    if len(ma) == 1 :
        return ma[0]
    elif ma[0] > ma[1]:
        return besar([ma[0]] + ma[2:])
    else :
        return besar([ma[1]] + ma[2:])


def Price (r,e):
    if isempty(r):
        return 0
    elif type(r[0]) == list:
        return besar(r[0]) + Price(r[1:],e)
    else :
        return Price(r[1:],e+[r[0]])

print(Price(Ninja,[]) * 10000000)
#[[2,3,4,6],[1,1,3,9,2,7],[2,1],[4,4,6],[3,3]]
# [[2,3,4,6,7],[1,1,3,2,7],[5,2,1],[4,4,6],[3,3]]
