# Desafio 1

msg = 'Hello World'
print(msg)

print('')

# Desafio 2
nome = input('Digite seu nome: ')
print('Bem vindo(a) {}!'.format(nome))

print('')

# Desafio 3
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print('A soma entre {} e {} e igual a {}'.format(n1, n2, soma))

print('')

# Desafio 4
msg1 = str(input('Digite alguma coisa: '))
print('Seu tipo primitivo:', type(msg1))
print('É um Alpha? ( Todos caracteres são letras )', (msg1.isalpha()))
print('É um número?', (msg1.isnumeric()))
print('É Alpha Númerico? ( Tem letra ou Número )', (msg1.isalnum()))
print('Está em letra maisculula?', (msg1.isupper()))
print('Está em letra minuscula?', (msg1.islower()))
print('A palavra está capitalizada? ( Tem maiscula e Minuscula )', (msg1.istitle()))

# Desafio 5
num1 = int(input('Digite um valor: '))
antecessor = (num1-1)
sucessor = num1+1
print('Valor sucessor: {} \nValor antecessor: {}'.format(sucessor, antecessor))

# Desafio 6
nu1 = int(input('Digite um valor: '))
dobro = nu1*2
triplo = nu1*3
raiz = nu1**(1/2)
print('Dobro do valor: {}\nTriplo do valor: {}\nRaiz do valor: {}'.format(dobro, triplo, raiz))

# Desafio 7