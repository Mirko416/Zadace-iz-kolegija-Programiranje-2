'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje
kao prvo slovo vašeg imena, a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

regex_izraz = r'^M.*[0-5].*\s.*Č$'

test = ["Mirko 4Ivan","Ivan Ivic","Mirko123 Č"]

for string in test:
    if re.match(regex_izraz,string):
        print("String je ispravan format.")
    else:
        print("Lana print.docx")
