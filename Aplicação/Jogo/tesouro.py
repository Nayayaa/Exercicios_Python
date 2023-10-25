import random

while True: 
    posicao = [random.radiant(0, 5), random.randint(0, 5)]
    if posicao != [0, 0]:
        break

if __name__ == "__main__":
    print(posicao)