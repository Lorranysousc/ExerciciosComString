'''Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de
formatação.'''

cpf = str(input('Insira seu CPF(xxx.xxx.xxx-xx) : '))
validade = 'Válido'

if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    validade = 'Inválido'
print(f'CPF {validade}!')
