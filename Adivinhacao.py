
import random

def jogar():
    print('*********************************')
    print('Bem vindo no Jogo de Adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1,101) # variável (numero_secreto) recebe o valor 42(int)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000


    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1): # Loop de repetição
        print('Tentativas {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Digite seu número: ')) # conversão de str(string) para int(intereger0
        print('Você digitou:',chute)

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto


        if (acertou): # Condição caso seja verdadeiro
            print('Você acertou e fez {} pontos !!'.format(pontos))
            break
        else:                           # Condição caso seja falso
            if (maior):
                print('Você errou!! O seu chute foi maior que o número secreto')
            if (menor):
                print('Você errou!! O seu chute foi menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos= pontos - pontos_perdidos



    print()
    print('*********************************')
    print('*********Fim do Jogo*************')
    print('*********************************')
if(__name__ == '__main__'):
    jogar()