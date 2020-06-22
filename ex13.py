'''Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.'''

import random
from sys import exit
#Escolher da listadePalavras uma palavra aleatória
listadePalavras = ['PLACA', 'PANDEIRO', 'CADERNO','CAMISA', 'PIANO']
palavra = random.choice(listadePalavras) 

#Converter a palavra escolhida em uma nova lista
convert_palavra = list(palavra) 
random.shuffle(convert_palavra)
nova_palavra = ''.join(convert_palavra)
print(nova_palavra)

#Interação usuario
for cont in range (0, 6): 
    usuario  = str(input('A palavra é: ').upper()) 
    if usuario == palavra:
        print(f'Você GANHOU! A palavra escolhida foi {palavra}.')
        exit()
    else:
        print('Hummm... Não foi dessa vez, tente novamente!')
print('FIM DE JOGO')