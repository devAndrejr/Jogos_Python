import Forca
import Adivinhacao


print('*********************************')
print('******Escolha o seu Jogo!********')
print('*********************************')

print('(1) Forca (2) Adivinhação')

jogo= int(input('Qual jogo?'))

if jogo == 1:
    print('Jogando Forca')
    Forca.jogar()
elif jogo == 2:
    print('Jogando  Adivinhação')
    Adivinhacao.jogar()
    

