"""
Faça um programa que peça ao usuário para digitar um número inteiro e informe se o número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
try:
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')

except ValueError:
    print('Isso não é um número inteiro.')