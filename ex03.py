'''Faça um programa que solicite o nome do usuário e imprima-o na vertical.'''

nome = str(input('Digite seu nome aqui: '))
tamanho = len(nome)
for cont in range (0, tamanho):
    print(nome[0+cont])