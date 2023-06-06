def jogar():
    print("*" * 33)
    print("Bem vindo ao jogo de Forca!")
    print("*" * 33)


palavra_secreta = "banana"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
enforcou = False
acertou = False

print(letras_acertadas)

while (not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip()

# Verifying if exists the letter in the secret word
    index = 0  # position
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1

    print(letras_acertadas)

print("Fim do jogo")
# This snippet is used to run the file directly
if (__name__ == "__main__"):
    jogar()
