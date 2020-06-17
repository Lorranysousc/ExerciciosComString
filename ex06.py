'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
o nome do mês por extenso.'''

from sys import exit

dia = int(input('Dia de seu nascimento: '))
if dia > 31:
    exit()
else:
    mes = int(input('Mês de seu nascimento: '))
    if mes > 12:
        exit()
    else:
        ano = int(input('Ano de seu nascimento: '))
