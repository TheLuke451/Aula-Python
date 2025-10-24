""" Calculadora com While """

while True:
    print()
    print('Selecione a operação desejada:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    escolha = input('Digite sua escolha (1/2/3/4/5): ')

    if escolha == '5':
        print('Saindo da calculadora. Até mais!')
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if escolha == '1':
            resultado = num1 + num2
            operacao = 'Soma'
        elif escolha == '2':
            resultado = num1 - num2
            operacao = 'Subtração'
        elif escolha == '3':
            resultado = num1 * num2
            operacao = 'Multiplicação'
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2 
                operacao = 'Divisão'
            else:
                print('Erro: Divisão por zero não é permitida.')
                continue

        print(f'O resultado da {operacao} entre {num1} e {num2} é: {resultado}')
    else:
        print('Opção inválida. Por favor, tente novamente.') 