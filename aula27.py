"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local do radar 1
RADAR_RANGE = 1  # alcance do radar, ou seja, até onde ele "enxerga"

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = vel_carro_pass_radar_1 and carro_passou_radar_1


if vel_carro_pass_radar_1:
    print("Você está acima da velocidade permitida.")

if carro_passou_radar_1:
    print("O carro passou no radar 1")

if carro_multado_radar_1:
    print('Carro multado em radar 1')
    
    