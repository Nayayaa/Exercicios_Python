print("verificando se o ano é bissexto")
# Definindo as variaveis.
ano = int(input("Digite o ano:"))

#Calculo do ano bissexto.
print(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("Equação do segundo grau ax² + bx + c = 0")
# Definindo as variaveis. 
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Fórmula do Delta.
delta = ( b ** 2 - 4*a*c )

# Resolvendo o Bhaskara.
x1 = ( -b + delta ** ( 1 / 2 )) / (2 * a)
x2 = ( -b - delta ** ( 1 / 2 )) / (2 * a)

#Print o resultado
print("O resultado de x1 é:", x1)
print("O resultado de x2 é:", x2)

