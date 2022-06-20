from dotenv import load_dotenv
import os

load_dotenv()

nome = os.getenv("NOME")

if nome == 'Laís':
    print('Olá, Laís!')
else:
    print('Olá, visitante!')
    