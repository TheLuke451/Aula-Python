"""
Operador Lógico 'not'
Usado para inverter o valor lógico de uma expressão.
not true = False
not false = True
"""
print(not True)  # Saída: False
print(not False) # Saída: True

senha = input("Senha: ")

if not senha:
    print("Você não digitou nada.") 