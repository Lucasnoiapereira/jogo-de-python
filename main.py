import random

def palavraEscolhida(palavras):
    escolha = random.choice(palavras)
    escolha_minuscula = escolha.lower()
    escolha_escondida = '_'*len(escolha_minuscula)
    return escolha_minuscula, escolha_escondida
palavras = ["Casa", "Familia", "Estudos", "Alimentacao", "Vida", "Cambalhota"]

palavra_a_ser_advinhada, palavra_ocultada = palavraEscolhida(palavras)


