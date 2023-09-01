#Primeiro exercicio
def salario(salario_hora, trabalho_hora):
    salario_mensal = salario_hora * trabalho_hora
    return salario_mensal

salario_hora = float(input("Informe o salário por hora: "))
trabalho_hora = float(input("Informe o número de horas trabalhadas no mês: "))

salario_final = salario(salario_hora, trabalho_hora)

print("O salário a ser recebido é: R$", salario_final)



#Segundo exercicio
def calculo(num1, num2, num3):
    resultado1 = 2 * num1 * num2 / 2
    resultado2 = 3 * num1 + num3
    resultado3 = num3 ** 3
    return resultado1, resultado2, resultado3

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

resultado1, resultado2, resultado3 = calculo(num1, num2, num3)

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro elevado ao cubo é:", resultado3)




# Terceiro exercicio
def calculo_oposto(num1, num2, num3):
    resultado1 = 2 * num1 * num2 / 2
    resultado2 = 3 * num1 + num3
    resultado3 = num3 ** 3
    return resultado1, resultado2, resultado3

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

resultado1, resultado2, resultado3 = calculo_oposto(num1, num2, num3)

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro elevado ao cubo é:", resultado3)