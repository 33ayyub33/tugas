#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10

Card = eval(input())

def IsEmpty(C):
    return C == []

def CountCard (C):
    if IsEmpty(C):
        return 0
    elif type (C[0]) == list:
        return CountCard (C[0]) + CountCard (C[1:])
    else :
        return 1 + CountCard (C[1:])

print (CountCard(Card))

#[1, [2, 3], [4, [5, 6, 7]]]

