import random

numeroAleatorio = random.randint(1, 100)
usuario = input("Nome do desafiante: ")
numerosTentados = []
max_tentativas = 6
while True:
    chute = int(input("Chute um numero: "))
    if chute in numerosTentados:
        print(f"Numero ja tentado, tente outro {usuario}!")
        continue
    if chute > numeroAleatorio:
        max_tentativas -= 1
        print(f"Numero maior que o alvo, tente novamente {usuario}!")
        numerosTentados.append(chute)
    if chute < numeroAleatorio:
        max_tentativas -= 1
        print(f"Numero menor que o alvo, tente novamente {usuario}")
        numerosTentados.append(chute)
    if chute == numeroAleatorio:
        print(
            f"Parabens voce acertou {usuario}!!!!!!\nO alvo era {numeroAleatorio}")
        quit()
    if max_tentativas == 0:
        print(
            f'Infelizmente voce perdeu {usuario}....\nO numero alvo era {numeroAleatorio}')
        quit()
