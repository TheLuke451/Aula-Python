#Exercício de cálculo do IMC
# Cálculo do Índice de Massa Corporal (IMC)
# Utilizando f-strings para formatação de strings 
nome = "Ricardo Fernandes de Araujo"
peso = 63.10
altura = 1.68
imc = peso / (altura ** 2)

print(f"{nome} tem {peso}kg e {altura}m de altura")
print(f"O IMC de {nome} é {imc:.2f}")