def e_par(num):
    if num % 2 == 0:
        print("É par")
    else:
        print("Não é par")
    print("final da função")

e_par(4)
e_par(5)

def conceito(nota):
    if nota > 9:
        print("Conceito A")
    elif nota > 8:
        print("Conceito B")
    elif nota > 7:
        print("Conceito C")
    else:
        print("Conceito D")

def cli():
    opcao = input("Digite 1 para abrir um arquivo, 2 para editar: ")
    match opcao:
        case "1":
            print("Opção 1")
        case "2":
            print("Opção 2")
        case _:
            print("Opção inválida!")
    
#Exercicio 1
def e_par(num):
    if num % 2 == 0:
        return True
    return False

def e_part2(num):
    return num % 2 == 0

#Exercicio 2
def maior(num1, num2):
    if num1 > num2:
        return num1
    return num2

def maior2(num1, num2):
    return num1 if num1 > num2 else num2
print(maior2(8,10))

#Exercicio 3
def valor(num):
    if num > 0:
        print("O número é positivo")
    elif num < 0:
        print("O número é negativo")

def valor(num):
    if num >= 0:
        return "Positivo"
    return "Negativo"

print(valor(10))
print(valor(-10))

#Exercicio 4
def vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "vogal"
    return "consoante"


def vogal2(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return "vogal"
        case _:
            return "consoante"

print(vogal2("e"))
    
#Exercicio 5
def media(nota1,nota2,nota3):
    m = (nota1 + nota2 + nota3) / 3
    if m == 10:
        print("Aprovado com Distinção")
    elif m >= 7:
        print("Aprovado")
    elif m < 7:
        print("Reprovado")
    else:
        print("Nota inválida!")

nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))

media(nota1,nota2,nota3)