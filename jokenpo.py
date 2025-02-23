import random

def escolhaMaquina(possibilidades):
    escolha = random.choice(possibilidades)
    return escolha

possibilidades = ['pedra', 'papel', 'tesoura']
usuario = input("Nome do usuario: ")
jogadas = 0
while True:
    escolha_maquina = escolhaMaquina(possibilidades)
    escolha_jogador = input("Pedra, Papel, Tesoura: ").lower()
    certo = 0
    escolha_jogada = 0
    escolha_da_maquina = 0
    for i in range(len(possibilidades)):
        if escolha_jogador == possibilidades[i]:
            certo += 1
            escolha_jogada = i
        if escolha_maquina == possibilidades[i]:
            escolha_da_maquina = i

    if certo == 0:
        print("Escolha inadequada tente novamente")
        continue
    if escolha_jogador == escolha_maquina:
        print(f"Empate, tente novamente {usuario}, adversario jogou {escolha_maquina}")
        jogadas += 1
    elif escolha_jogador != escolha_maquina:
        if escolha_jogada > escolha_da_maquina:
            print(f"Voce venceu parabens {usuario}!!! Seu adversario jogou {escolha_maquina}")
            jogadas += 1
            quit()
        else:
            print(f"Infelizmente voce perdeu {usuario}, seu adversario jogou {escolha_maquina}!")
            jogadas += 1
            quit()