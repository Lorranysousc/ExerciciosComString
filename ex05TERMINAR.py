'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.'''

nome = str(input('Digite seu nome aqui: '))
tamanho = len(nome)
for cont in range (tamanho, 0, -1):
    print(nome[:0:cont])