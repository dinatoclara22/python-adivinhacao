import random


def jogar():
    print("*" * 33)
    print("Bem vindo ao jogo de Forca!")
    print("*" * 33)

    # Opening the file
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    # Choosing a random word
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]  # List Comprehension

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            # Verifying if exists the letter in the secret word
            index = 0  # position
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!! :(")
    print("Fim do jogo")


# This snippet is used to run the file directly
if (__name__ == "__main__"):
    jogar()
