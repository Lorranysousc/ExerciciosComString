'''Faça um programa que leia um número de telefone, e corrija o número no caso
deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
separador.'''

from sys import exit

numeroTelefone = str(input('Digite seu Telefone(xxxx-xxxx): '))
tamanho = len(numeroTelefone)

if tamanho <= 6 or tamanho >= 9: #Encerra programa
    exit()

if ('-' in numeroTelefone) == False and tamanho == 7:
    num = '3' + numeroTelefone
elif ('-' in numeroTelefone) == True and tamanho == 8 and numeroTelefone[3] == '-':
    num = '3' + numeroTelefone
else:
    exit()
print(f'Seu Telefone possui 7 dígitos. Vou acrescentar o digito 3 na frente. \nTelefone: {num}')
