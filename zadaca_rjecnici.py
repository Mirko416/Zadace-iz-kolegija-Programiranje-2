'''
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu
ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''

lista_imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']


import random

ocjene = [random.randint(1,5) for _ in lista_imena]

rj_ocjena = {}
for ocjena in ocjene:
    if ocjena in rj_ocjena:
        rj_ocjena[ocjena] += 1
    else:
        rj_ocjena[ocjena] = 1

print("Broj pojavljivanja ocjena:")
for ocjena,broj in rj_ocjena.items():
    print("Ocjena",str(ocjena),":",str(broj),"studenata")

ukupno_studenata = len(lista_imena)
broj_prolaznih = sum(broj for ocjena, broj in rj_ocjena.items() if ocjena > 1)
postotak_prolaznosti = (broj_prolaznih / ukupno_studenata) * 100

print("Prolaznost:",str(postotak_prolaznosti),"%")
