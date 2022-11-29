#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10


hindari = eval(input())
kelipatan = int(input())

def IsEmpty(m):
    return m == []

def hmonster (m):
    if IsEmpty(m):
        return []
    elif type (m[0]) == list:
        return [hmonster (m[0])] + hmonster (m[1:])
    else :
        if m[0] % kelipatan == 0:
            return hmonster (m[1:])
        else:
            return [m[0]] + hmonster (m[1:])
print (hmonster(hindari))

#[[2, 3, 4], [5, 6, 8, [1, 2, 3]], [4, 5, 10], [10, 10, 8]]
#2