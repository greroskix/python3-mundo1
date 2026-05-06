nome = str(input('Qual e seu nome: '))
print('Prazer em te conhecer {}!'.format(nome))

print('')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
mul = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.2f}'.format(s, sub, mul, di), end=' ')
print('A exponenciação é {} e a divisão inteira é {}'.format(e, di))
