n1 = int(input('Digite um Número: '))
n2 = int(input('Digite outro Número: '))
soma = n1 + n2
# print('A soma entra', n1, 'e', n2, 'vale', soma) Metodo ruim de se fazer
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))