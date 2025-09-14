"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'ricardo'
outra_string = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' output: TypeError

print(string)
print(outra_string)
print(string.capitalize())
