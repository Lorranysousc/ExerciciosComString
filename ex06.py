'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
o nome do mês por extenso.'''

from sys import exit #Biblioteca para encerrar o programa se o usuário digitar um valor incorreto.
from datetime import date #Biblioteca com a data atual.

dia = int(input('Dia de seu nascimento: '))
if dia > 31:
    exit()

mes = int(input('Mês de seu nascimento: '))
meses = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'
dividirMeses = meses.split()
if mes > 12:
    exit()

ano = int(input('Ano de seu nascimento: '))
anoatual = date.today().year #Chamando ano atual.
if ano > anoatual:
    exit()
    
print(f'Você nasceu em {dia} de {dividirMeses[mes-1]} de {ano}.')