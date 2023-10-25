def desenha(personagem, tesouro):
    for x in range(6):
        for y in range(6):
            if personagem == [x, y]:
                print("@", end=" ")
            elif tesouro == [ x, y]:
                print ("X", end= " ")
            else: 
                print(".", end=" ")
        print()
    
if __name__ == "__main__":
    desenha([0, 0], [2, 4])
    print("-" * 12)
    desenha([2, 1], [5, 0])
    