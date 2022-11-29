#Nama                   : Ayyub Al Anshor
#NIM                    : 24060122130054
#Kelas/KelasPrakDaspro  : C/A1
#Tugas                  : 10


candy = eval(input())

def isempty(e):
    return e == []
def pedagang (d):
    if d == []:
        return 0
    return d[0] + pedagang(d[1:])

def om_om (pm):
    if isempty(pm):
        return 0
    elif type (pm[0]) == list:
        if pedagang (pm[0]) % 2 == 0:
            return pedagang(pm[0]) * 2000 + om_om(pm[1:])
        else:
            return pedagang(pm[0]) * 1000 + om_om(pm[1:])
    else :
        if int(pm[0]) % 2 == 0:
            return pm[0] * 4000 + om_om(pm[1:])
        else :
            return pm[0] * 3000 + om_om (pm[1:])

print (om_om(candy))
#[2,3,[1,4],[2,2],9]
