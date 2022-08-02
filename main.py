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
         'liz': 'pass123'
         }

username = input('Zadej přihlašovací jméno: ')
password = input('Zadej heslo: ')

if users.get(username) == password:
    print(f'Ahoj {username.upper()} pojďme analyzovat text...')

else:
    print(f'Neplatné uživatelské jméno nebo heslo.')

