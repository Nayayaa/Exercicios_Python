from Jogo import personagem, mapa, tesouro

def valida_dados(dado):
    return dado.lower() in "wasd" and len(dado) == 1 

def main():
    while True:
        mapa.desenha(personagem.posicao, tesouro.posicao)
        comando = input("Insira para onde você quer ir (W, A, S, D) ou Q para sair: ")
        if comando == "Q":
            break

        if valida_dados(comando):
            personagem.move(comando)
            if personagem.posicao == tesouro.posicao:
                print("Você encontrou o tesouro!")
                break
        else:
            print("Comando Inválido!")

if __name__ == "__manin__":
    main()