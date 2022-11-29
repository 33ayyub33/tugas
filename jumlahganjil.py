#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10

kartu = eval(input())

def isempty(c):
    return c ==[]
def kelipatanganjil (g):
    if isempty(g):
        return 0
    elif type (g[0]) == list:
        return kelipatanganjil (g[0]) + kelipatanganjil (g[1:])
    else :
        if g[0] % 2 == 0:
            return kelipatanganjil (g[1:])
        else :
            return g[0] + kelipatanganjil (g[1:])
print (kelipatanganjil(kartu))

#[1,[5,2,3],10,9,[7],[3,3]] 