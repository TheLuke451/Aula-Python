"""
Faça um programa que peça ao usuário para digitar a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
"Bom dia", "Boa tarde" ou "Boa noite". Considere:
    - Bom dia: 0-11
    - Boa tarde: 12-17
    - Boa noite: 18-23
"""

horario = int(input('Digite a hora atual como número inteiro: '))

if horario >= 0 and horario <= 11:
    print('Bom dia!')
elif horario >= 12 and horario <= 17:
    print('Boa tarde!')
elif horario >= 18 and horario <= 23:
    print('Boa noite!')
else:
    print('Hora inválida!')