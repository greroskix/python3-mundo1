# Desafio 1
msg = 'Hello World'
print(msg)

# Desafio 2
nome = input('Digite seu nome: ')
print('Bem vindo(a) {}!'.format(nome))

# Desafio 3
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print('A soma entre {} e {} e igual a {}'.format(n1, n2, soma))

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
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('A sua média é {}'.format(media))

# Desafio 8
tamanho = int(input('Digite um tamanho em metros: '))
cm = tamanho*100
mm = tamanho*1000
print('{0}m em Centimentros é: {1}\n{0}m em Milimetros é: {2}'.format(tamanho, cm, mm))

# Desafio 9
tabuada = int(input('Digite um número para ver sua tabuada: '))
print('Tabuada do {} até o 10!'.format(tabuada))
for i in range (1,11):
    conta = tabuada *  i
    print('{} x {} = {}'.format(tabuada, i, conta))

# Desafio 10
carteira = float(input('Digite quanto você tem na sua carteira (R$): '))
dolar = 4.92
conversor = carteira/dolar
print('Hoje o Dolar está valendo {} e você com {} pode comprar {:.2f} dolares!'.format(dolar, carteira, conversor))

# Desafio 11
altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))
area = largura*altura
tinta = area/2
print('O valor da área da sua parede e de {} e você vai precisar de {} litros de tinta para pintar ela'.format(area, tinta))

# Desafio 12
preco = float(input('Digite o valor do produto: '))
desconto = (5/100)*preco
valor_final = preco - desconto
print('O produto com desconto de 5% fica ao todo: {}'.format(valor_final))

# Desafio 13
salario = int('Digite seu salário: ')
aumento = (15/100)*salario
salario_final = salario + aumento
print('Seu salário com 15% de aumento vai ficar {}'.format(salario_final))

# Desafio 14
print('Vamos converter uma temperatura de C° para F°')
c = float(input('Digite o valor da temperatura em C°: '))
f = (c*9/5)+32
print(f'{c} C° em F° é {f}')

# Desafio 15
print('Carros Alugados!')
km = float(input('Digite qual a quantidade de km rodados: '))
dias = int(input('Digite qual a quantidade de dias: '))
sistema = (dias * 60) + (km * 0.15)
print(f'Você devera pagar R${sistema:.2f}')
