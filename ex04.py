'''Modifique o programa anterior de forma a mostrar o nome em formato de escada.'''

nome = str(input('Digite seu nome: ').upper())
tamanho = len(nome)
for cont in range(1, tamanho+1):
    print(nome[0:cont])