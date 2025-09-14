"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito - Quando um programa não tem fim
"""
condicao = True # Desnecessário usar esta variavel no while

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print("Acabou")


