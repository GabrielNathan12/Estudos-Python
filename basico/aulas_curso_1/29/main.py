# Usar letras maiusculas para representar valores constantes

velocidade = 61
local_carro = 90

RADAR_1 = 10
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_pss_radar_1 = velocidade > RADAR_1;
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_pss_radar_1:
    print('Passou do radar 1')

if carro_multado and velocidade_carro_pss_radar_1:
    print('O carro foi multado')