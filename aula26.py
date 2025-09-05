"""
Introdução ao try/except
try -> tentar executar o código
except -> O que fazer em caso de falha
Apenas aprendizado, não é uma boa prática usar dessa forma abaixo
"""


numero_str = input(
    "Vou dobrar o número que você digitar: "
)

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f"O dobro de {numero_float} é {numero_float * 2}")
except:
    print("Isso não é um número válido.")
