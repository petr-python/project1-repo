"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Hasoň
email: petrhason@gmail.com
discord: Petr H. #4342
"""
from task_template import TEXTS

users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123',
         'renata': 'heslo'
         }

username = input('Zadej přihlašovací jméno: ')
password = input('Zadej heslo: ')

if users.get(username) == password:
    print(f'Ahoj {username.upper()} pojďme analyzovat text...')

else:
    print(f'Neplatné uživatelské jméno nebo heslo.')
    quit()


cislo_textu = input(f'Zvol od 1 do 3 číslo textu pro analýzu: ')

if cislo_textu.isnumeric() and 1 <= int(cislo_textu) <= 3:
    vybrany_text = TEXTS[int(cislo_textu) - 1]


else:
    print(f'Chybné zadání. Ukončuji program.')

print(f'Vybraný text: \n{vybrany_text} \n')

# počet slov
pocet_slov = len(vybrany_text.split())
print(f'Počet slov: {pocet_slov}')

# statistiky pro text
zacinajici_pismena = 0
velka_pismena = 0
mala_pismena = 0
pocet_cisel = 0
list_cisel = []

# počet slov začínajících velkým písmenem,
for slovo in vybrany_text.split():
    if slovo[0].isupper():
        zacinajici_pismena = zacinajici_pismena + 1

# počet slov psaných velkými písmeny,
    elif slovo.isupper():
        velka_pismena = velka_pismena + 1

# počet slov psaných malými písmeny,
    elif slovo.islower():
        mala_pismena += 1

# počet čísel (ne cifer),
    elif slovo.isnumeric():
        pocet_cisel += 1

# sumu všech čísel (ne cifer) v textu.
        list_cisel.append(int(slovo))

print(f'Slova začínající Velkým písmenem {zacinajici_pismena}')
print(f'Slova psané VELKÝMI písmeny: {velka_pismena}')
print(f'Slova psané malými písmeny: {mala_pismena}')
print(f'Počet číslic: {pocet_cisel}')
print(f'Suma čísel: {sum(list_cisel)}')
