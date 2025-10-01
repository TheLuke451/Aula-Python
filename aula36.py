"""
Iterando strings com while
"""

nome = 'Ricardo'  # Iterável

tamanho_nome = len(nome)

i = 0
novo_nome = ''

while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1

print(novo_nome)