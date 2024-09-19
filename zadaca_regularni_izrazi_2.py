'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata
ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba
gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora
postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
Istražiti greedy i non-greedy quantifiers.
'''

import re

email_regex = r'^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$'

eduid_regex = r'^i[a-z]+[0-9]*@sum\.ba$'

def provjeri_email():
    email = input("Unesite e-mail (ime.prezime@fpmoz.sum.ba): ")
    if re.match(email_regex,email):
        print("E-mail je ispravan.")
    else:
        print("E-mail nije ispravan.")

def provjeri_eduid():
    eduid = input("Unesite eduID (iprezimeX@sum.ba): ")
    if re.match(eduid_regex,eduid):
        print("eduID je ispravan.")
    else:
        print("eduID nije ispravan.")

provjeri_email()
provjeri_eduid()
