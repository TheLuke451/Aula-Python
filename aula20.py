"""
Aula 20

Operadores Lógicos
Operadores lógicos são usados para combinar expressões booleanas. Os principais operadores lógicos em Python são:
- `and`: Retorna True se ambas as expressões forem verdadeiras.
- `or`: Retorna True se pelo menos uma das expressões for verdadeira.
- `not`: Inverte o valor lógico da expressão.
- `None`: Representa a ausência de valor ou um valor nulo. É um tipo especial em Python.
"""

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "1234"

if entrada == "E" or "e" and senha_digitada == senha_permitida:
    print("Você escolheu entrar.")
elif entrada == "E" or "e" and senha_digitada != senha_permitida:
    print("Senha incorreta. Acesso negado.")
elif entrada == "S" or "s":
    print("Você escolheu sair.")
else:
    print("Opção Inválida. Por favor, escolha 'E' para entrar ou 'S' para sair.")

