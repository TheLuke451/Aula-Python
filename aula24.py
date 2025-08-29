"""
Formatação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal 
(Caractere) (><^) (quantidade)
> - direita
< - esquerda
^ - centro
= - Força o número a ser formatado a ser colocado após o sinal
sinal - + ou -
Ex. : 0>-100,.1f
Conversion flags - !r !s !a = __repr__ __str__ __ascii__
"""
variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}') # Direita
print(f'{variavel: <10}') # Esquerda
print(f'{variavel: ^10}') # Centro

print(F"{1000.1010103104:0=+10,.1f}")
print(f"O hexadecimal de 1500 é {1500:05X}")
print(f'{variavel!r}')
