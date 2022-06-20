from dotenv import load_dotenv
import os

load_dotenv()

nome = os.getenv("NOME")

if nome == 'Laís':
    print('Olá, Laís!')
elif nome == 'João':
    print('Olá, João! Tudo bem?')
else:
    print('Olá, visitante!')
    
    
"""quero uma função que calcula a média entre dois números"""

def media(n1, n2):
    return (n1 + n2) / 2

a = media(3,2)
print(a)