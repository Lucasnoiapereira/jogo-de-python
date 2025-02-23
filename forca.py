import random


def palavraEscolhida(palavras):
    escolha = random.choice(palavras)
    escolha_minuscula = escolha.lower()
    escolha_escondida = '_'*len(escolha_minuscula)
    return escolha_minuscula, escolha_escondida


palavras = ["Casa", "Familia", "Estudos", "Alimentacao", "Vida", "Cambalhota"]

palavra_a_ser_advinhada, palavra_ocultada = palavraEscolhida(palavras)

letras_tentadas = []
max_tentativas = 6

while True:
    print(palavra_ocultada)
    tentativa = input("Digite uma letra: ")
    if tentativa in letras_tentadas:
        print("Voce ja digitou essa letra, tente outra: ")
        continue
    letras_tentadas.append(tentativa)
    if tentativa in palavra_a_ser_advinhada:
        lista = []
        for i in range(len(palavra_a_ser_advinhada)):
            if tentativa == palavra_a_ser_advinhada[i]:
                lista.append(tentativa)
            else:
                lista.append(palavra_ocultada[i])
        palavra_ocultada = ''.join(lista)
    else:
        max_tentativas -= 1
        print(
            f'Letra tentatada nao presente na palavra, voce ainda possui {max_tentativas} tentativas!')
    if palavra_a_ser_advinhada == palavra_ocultada:
        print("Parabens voce ganhou!!!!")
        break
    elif max_tentativas == 0:
        print(f'Voce perdeu!! A palavra era {palavra_a_ser_advinhada}')
        break
