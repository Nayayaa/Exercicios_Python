# Exercício 1
import random 
dados = 100
lista = [0,0,0,0,0,0]

for _ in range(dados):
    resultado = random.randint(1, 6)
    lista[resultado - 1] += 1 

for i in range(6):
    print(f"O valor {i +1} foi obtido {lista[i]} vezes.")


# Exercício 2
import json

def adicionar_alunos(dicionario_alunos, matricula, nome, email):
    dicionario_alunos[matricula] = {
        "nome": nome,
        "e-mail": email
    }

try:
    with open('alunos.json', 'r') as arquivo:
        dados_alunos = json.load(arquivo)
except FileNotFoundError:
    dados_alunos = {}

while True:
    matricula = input("Digite a matricula do aluno: ")
    if not matricula:
        break
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")


    adicionar_alunos(dados_alunos, matricula, nome, email)


with open('alunos.json', 'w') as arquivo:
    json.dump(dados_alunos, arquivo, indent=4)


print('Dados dos alunos salvos com sucesso no arquivo alunos.json')


# Exercício 3
import datetime

def recebe_data():
    try:
        usuario = input("Digite uma data no formato DD/MM/AAAA: ")
        data = datetime.datetime.strptime(usuario,"%d/%m/%Y")
        print(data.strftime('%d de %B de %Y'))
    except ValueError:
        return None

recebe_data()
