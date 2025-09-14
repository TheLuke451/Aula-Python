"""
Flag (Bandeira) - Marcar um local
None = Não valor/Nulo
is e is not = é ou não é (tipo,valor, identidade)
id = identidade
"""
condição = False
passou_no_if = None  # Bandeira

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')



if passou_no_if is None:
    print('Não passou no if')


if passou_no_if is not None:
    print('Passou no if')
