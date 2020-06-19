'''Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.'''

string = str(input('Digite sua frase aqui: ').strip().upper()) #.strip() tira espaços excedentes antes e depois da string

dividir = string.split()
juntar = ''.join(dividir) #Tirando os espaços da string
inverterString = juntar[::-1].upper()

if juntar == inverterString:
    palindromo = 'é um PALÍNDROMO'
else:
    palindromo = 'NÃO é um PALÍNDROMO'
print(f'A string {juntar} invertida é {inverterString}, por isso {palindromo}.')