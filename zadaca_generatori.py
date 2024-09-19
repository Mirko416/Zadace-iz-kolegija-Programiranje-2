'''
Napraviti generator funkcije za ispis svih parnih i svih neparnih
brojeva manjih od prosljeđenog parametra.
'''

def generator(maximum_broj):
    for i in range(maximum_broj):
        if i % 2==0:
            yield "Parni broj:",str(i)

        else:
            yield f"Neparni broj:",str(i)
maximum_broj = 20
for broj in generator(maximum_broj):
    print(broj)
