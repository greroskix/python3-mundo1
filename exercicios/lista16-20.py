from math import floor, sqrt, sin, cos, tan, radians
from random import choice, shuffle
from winsound import PlaySound, SND_ASYNC

# Desafio 16
num1 = float(input('Digite um Número: '))
print(f'{floor(num1)}') # Outro jeito seria usando int(num), pois ele vai pegar o float e transformando em um inteiro

# Desafio 17
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotesuna = (sqrt(cateto_oposto**2 + cateto_adjacente**2))
print(f'Valor da hipotenusa: {hipotesuna:.2f}') # Outro jeito seria usando o hypot, que ficaria assim: hypot(ca,co)

# Desafio 18
angulo = float(input('Digite um Ângulo: '))
radiano = radians(angulo)
print(f'Valor do Seno: {sin(radiano):.2f}, Valor do Coseno: {cos(radiano):.2f}, Valor da Tangente: {tan(radiano):.2f}')
# Nesse exercicio eu esqueci de conveter o angulo para radiano antes, usando o radians

# Desafio 19
aluno1 = str(input('Digite o nome do Aluno 1: '))
aluno2 = str(input('Digite o nome do Aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno sorteado foi: {choice(sorteio)}')

# Desafio 20
apresentacao1 = str(input('Digite o nome do 1° grupo: '))
apresentacao2 = str(input('Digite o nome do 2° grupo: '))
apresentencao3 = str(input('Digite o nome do 3° grupo: '))
apresentecao4 = str(input('Digite o nome do 4° grupo: '))
seminario_ordem = [apresentacao1, apresentacao2, apresentencao3, apresentecao4]
shuffle(seminario_ordem)
print(f'A ordem do seminario vai ser: {seminario_ordem}')

# Desafio 21
alee = 'alee.wav'
PlaySound(alee, SND_ASYNC)
input('Presione enter para parar a música.')