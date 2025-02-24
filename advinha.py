import random

def advinha(x):
    numero_aleatorio = random.randint(1, x)
    tentativas = 0
    while tentativas != numero_aleatorio:
        tentativas = int(input(f"Chute um numero entre 1 e {x}: "))
        if tentativas < numero_aleatorio:
            print("Tente novamente, numero muito baixo.")
        elif tentativas > numero_aleatorio:
            print("Tente novamente, numero muito alto")
    print(f'Parabens voce acertou o numero {numero_aleatorio}!!!')


def computadorAdvinha(x):
    numero_max = x
    numero_min = 1
    atualizacao = ''
    while atualizacao != 'c':
        tentativa_computador = random.randint(numero_min, numero_max)
        print(f'Meu chute eh {tentativa_computador}')
        atualizacao = input("O chute esta:\n a - muito baixo \n b - muito alto \n c - certo\n")
        if atualizacao == 'a':
            numero_min = tentativa_computador + 1
        elif atualizacao == 'b':
            numero_max = tentativa_computador - 1
    print(f"Seu numero eh {tentativa_computador}")
computadorAdvinha(10)
advinha(10)