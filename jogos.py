import adivinhacao
import forca


def escolhe_jogo():
    print("*" * 33)
    print("Escolha o seu jogo!")
    print("*" * 33)

    print("1 - Forca\n2 - Adivinhação")
    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    else:
        print("Jogo inválido!")


# This snippet is used to run the file directly
if (__name__ == "__main__"):
    escolhe_jogo()
