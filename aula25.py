"""
Fatiamento de strings

012345678
Olá mundo
-987654321 
Fatiamento [i:f:p] (::) (inicio:fim:passo)

Obs.: a função len retorna a quantidade de caracteres da string
"""
variavel = "Olá mundo"
print(variavel[4:]) # Output: mundo
print(variavel[4:7]) # Output: mun
print(variavel[0:5]) # Output: Olá m
print(variavel [-8:-2]) # Output: lá mun
print(variavel[0:9:3]) # Output: O n
print(variavel[-1:-10:-1]) # Output: odnum álO  

print(len(variavel)) # Output: 9

