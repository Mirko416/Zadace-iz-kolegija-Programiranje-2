'''
Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program
i pozvati je nakon traženja unosa
od korisnika.
'''

from funkcijsko import treca, pozdrav, dobrodosao

ime = input("Unesite ime: ")
print(treca(pozdrav, ime))
print(treca(dobrodosao, ime))
