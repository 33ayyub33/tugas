#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10

Angka = eval(input())

def isempty(t):
    return t ==[]

def islist(s):
    if type (s[0]) == list:
        return True
    else: 
        return False

def IsPrima(n, i = 2) :
    if (n < 2):
        return False
    elif (n == 2):
        return True
    elif (n % i == 0):
        return False
    elif (i * i > n) :
        return True
    return IsPrima(n, i + 1)

def jumprim(p):
    if isempty(p):
        return 0
    #elif type (p[0]) == list:
    elif islist(p):
        return jumprim (p[0]) + jumprim (p[1:])
    else :
        if IsPrima(p[0],2):
            return p[0] + jumprim (p[1:])
        else:
            return  jumprim (p[1:])

print (jumprim(Angka))

#[[[[[[[[[[9,7,10]]]]]]]]]] 
#[123,321,[222],[100,200,300,400,500,[313]]] 