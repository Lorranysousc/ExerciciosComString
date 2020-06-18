'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.'''

string = str(input('Digite algo aqui: ').upper()) #.upper() transforma a string em maiuscula

espacos = string.count(' ')
vogais = string.count('A')+string.count('E')+string.count('I')+string.count('O')+string.count('U')

print(f'Em {string} existem: \n{espacos} espaços em branco. \n{vogais} vogais.')