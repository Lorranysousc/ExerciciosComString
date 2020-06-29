'''Altere o programa anterior de modo que a escada seja invertida.'''

nome = str(input('Digite seu nome: ').upper())
tamanho = len(nome)
for cont in range(0,tamanho):
	print(nome[0:tamanho-cont])
