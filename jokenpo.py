import random


def jogar():
    usuario = input('O que voce deseja jogar? pedra, papel ou tesoura: ')
    maquinha = random.choice(['pedra', 'tesoura', 'papel'])
    if usuario == maquinha:
        return 'É um empate!!'
    if vitoria(usuario, maquinha):
        return 'Voce venceu!!!!!'

    return 'Voce perdeu!!!'


def vitoria(usuario, maquina):
    # return True se vitoria
    # pedra ganha de tesoura, tesoura ganha de papel e papel ganha de pedra

    if (usuario == 'pedra' and maquina == 'tesoura') or (usuario == 'tesoura' and maquina == 'papel') or (usuario == 'papel' and maquina == 'pedra'):
        return True
    return False


print(jogar())
