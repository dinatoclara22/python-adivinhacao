# Imports
import random


def jogar():

    print("*" * 33)
    print("Bem vindo ao jogo de Adivinhação!")
    print("*" * 33)

    # random.randrange(1, 101) => Creating a random number between 1 and 100 using the random module
    # Initializing the variables
    numero_secreto = random.randrange(1, 101)
    total_de_tentivas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("1 - Fácil\n2 - Médio\n3 - Difícil")

    nivel = int(input("Defina o nível: "))

    # Defining the number of attempts according to the level
    if (nivel == 1):
        total_de_tentivas = 20
    elif (nivel == 2):
        total_de_tentivas = 10
    else:
        total_de_tentivas = 5

    # Looping the attempts
    for rodada in range(1, total_de_tentivas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentivas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o número secreto.")

            # Calculating the points lost
            # Abs: brings the absolute value of the subtraction (-20 => 20)
            pontos_perdidos = abs(numero_secreto - chute)  # Ex: 40-20 = 20
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")


# This snippet is used to run the file directly
if (__name__ == "__main__"):
    jogar()
