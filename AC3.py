#AC3
#Exercicio 1
def reajuste(salario):
    if salario <= 280:
        percentual = 0.2 * salario
        
    elif salario > 280 and salario < 700:
        percentual = 0.15 * salario
          
    elif salario > 700 and salario < 1500:
        percentual = 0.1 * salario
        
    elif salario > 1500:
        percentual = 0.05 * salario

    aumento = percentual + salario
    print("O valor do aumento é: R$", percentual)
    print("Aumento de", percentual * 100/salario, "%")
    print("Novo salário é: R$", aumento)

salario = float(input("Informer o seu salário:"))
print("Valor do salário atual R$", salario)

reajuste(salario)

#Exercicio 2
def semana(dia):
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sábado")
    else:
        print("valor inválido")

dia = int(input("Digite um número do 1 ao 7 para o dia da semana:"))

semana(dia)

#Exercicio 3
def calculo():

    a = int(input("Digite o valor de a:"))
    if a == 0:
        return "A equação não é do segundo grau"
    else:
        b = int(input("Digite o valor de b:"))
        c = int(input("Digite o valor de c:"))
        delta = ( b ** 2 - 4*a*c)
        x1 = ( -b + delta ** (1 / 2)) / (2 * a)
        x2 = ( -b - delta ** (1 / 2)) / (2 * a)
        if delta == 0:
            return "A equação possui uma raiz real", x1
        if delta < 0:
            return "A equação não possui uma raiz real"
        if delta > 0:
            return "A equação possui duas raízes reais", "x1=", x1 ,"x2=", x2
        
print(calculo())
