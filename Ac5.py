# Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
num = int(input("Digite seu número: "))
lista = []
def sequencia_numero(num):
    for i in range(1, num + 1):
        lista.append(i)
        print(*lista)
sequencia_numero(num)

# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
num = int(input("Digite seu número: "))
def digito(num):
    contador = 0
    while num > 0:
        num = num // 10
        contador += 1
    print(contador)

digito(num)

#Faça um programa que solicite ao usuário 2 números inteiros. A seguir, calcule e mostre a divisão do primeiro pelo segundo. Para resolver este problema, utilize a instrução try-except, particularmente analizando as exceções do tipo ValueError e ZeroDivisionError. Inclua uma instrução finally para exibir o resultado da operação.
try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    resultado = num1 / num2

except ValueError:
    print("Erro: Um dos valores não é um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

finally:
    try:
        print("Resultado da divisão:",resultado)
    except NameError:
        print("A divisão não pôde ser calculada devido a erros anteriores.")