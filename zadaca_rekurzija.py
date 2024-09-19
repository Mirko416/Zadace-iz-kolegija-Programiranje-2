'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
'''

def sazada(a):
    if a == "":
        return a
    print(a)
    return sazada(a[1:]) + a[0]

print(sazada("kolokvij"))
