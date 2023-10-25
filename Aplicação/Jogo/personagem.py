posicao = [0, 0]

def move(dir):
    if dir.lower() == "w":
        if posicao[1] > 0:
            posicao[1] -= 1
    elif dir.lower() == "s":
        if posicao[1] < 5:
            posicao[1] += 1
    elif dir.lower() == "d":
        if posicao[0] < 5:
            posicao[0] += 1
    elif dir.lower() == "a":
        if posicao[0] > 0:
            posicao[0] -= 1

if __name__ == "__main__":
    print(posicao)
    move("d")
    print(posicao)
    move("a")
    print(posicao)
    move("w")
    print(posicao)
    move("s")
    print(posicao)