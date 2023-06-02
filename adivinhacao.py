# Imports
import random

print("*" * 33)
print("Bem vindo ao jogo de Adivinhação!")
print("*" * 33)

# Creating a random number between 1 and 100 using the random module
numero_secreto = random.randrange(1, 101)
total_de_tentivas = 3

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
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor que o número secreto.")

print("Fim do jogo!")
