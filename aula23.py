"""
Interpolação básica de Strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Ricardo'
preco = 1000.9589765
variavel = '%s,o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %05X" % (1500, 1500))