import random
import string
from palavras import palavras
# funcao para escolher uma palavra aleatorio para o jogo
def peguePalavra(palavras):
    palavra = random.choice(palavras)
    return palavra.upper()

def jogoDaForca():
    palavra = peguePalavra(palavras)
    letras_em_palavra = set(palavra) # letras na palavra para ser advinhada
    alfabeto = set(string.ascii_uppercase)
    letras_tentadas = set() # o que o usuario ja tentou jogar
    max_tentativa = 8
    while len(letras_em_palavra) > 0 and max_tentativa > 0:
        print("Letras usadas: ", ' '.join(letras_tentadas)) #mostra para o usuario as letras ja usadas e a quantidade de tentativas restantes
        print(f"Tentativas restantes: {max_tentativa}")
        # P A L A - R  A
        lista_da_palavra = [letra if letra in letras_tentadas else '-' for letra in palavra] 
        print("Palavra alvo: ", ' '.join(lista_da_palavra))
        # pegando a tentativa do usuario
        letra_usuario = input('Chute uma letra: ').upper()
        if letra_usuario in alfabeto - letras_tentadas:
            letras_tentadas.add(letra_usuario)
            if letra_usuario in letras_em_palavra:
                letras_em_palavra.remove(letra_usuario)
            else:
                max_tentativa -= 1
        elif letra_usuario in letras_tentadas:
            print("Caracter ja tentado anteriormente, tente novamente.")
        else:
            print("Caracter invalido, tente novamente.")
    print("A palavra era", palavra)
    
jogoDaForca()

