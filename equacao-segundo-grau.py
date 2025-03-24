from math import sqrt

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

delta = b**2 - 4 * a * c

if delta >= 0:
    raiz = (-b + sqrt(delta)) / (2 * a)
    print(f'a 1ª raiz é: {raiz}')
    raiz = (-b - sqrt(delta)) / (2 * a)
    print(f'a 2ª raiz é: {raiz}')
else:
    print('não existe raiz negativa!')
