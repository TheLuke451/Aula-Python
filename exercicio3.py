"""
Faça um programa que peça ao usuário para digitar seu nome.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Se tiver mais de 6 letras, escreva "Seu nome é muito grande".
"""
nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")