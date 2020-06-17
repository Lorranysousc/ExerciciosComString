'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

str1 = str(input('String 1: ').upper())
str2 = str(input('String 2: ').upper())
print(f'A frase "{str1}" tem {len(str1)} caracteres. \nA frase "{str2}" tem {len(str2)} caracteres.')

if len(str1) == len(str2):
    print('- As duas strings possuem o mesmo tamanho.')
else:
    print('- As duas strings são de tamanhos diferentes.')

if str1 == str2:
    print('- As duas strings possuem conteúdos iguais.')
else:
    print('- As duas strings possuem conteúdos diferentes.')
    