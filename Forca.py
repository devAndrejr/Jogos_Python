import random
def jogar():
    print('*********************************')
    print('Bem vindo no Jogo de Forca!******')
    print('*********************************')

    #Leitura do arquivo para escolha da palavra secreta
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]



    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()  # Retorna palavra sem espaçamento

        if(chute in palavra_secreta):
            index=0 # posição de cada letra
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index]=letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print()
        print('PARABÉNS VOCÊ ACERTOU !!!!')
    else:
        print('Você Perdeu.')


    print()
    print('*********************************')
    print('*********Fim do Jogo*************')
    print('*********************************')
if(__name__ == '__main__'):
    jogar()