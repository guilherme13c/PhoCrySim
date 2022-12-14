# inclui o arquivo de funcionamento do motor de simulacao
from components import *

# define os inputs
in1, in2 = 50, 50
# define o controle
ctrl = 50

# define o circuito
T1, D1 = Switch_P.calculate(ctrl, in1)
T2, D2 = Switch_P.calculate(T1, in2)

# exibe os valores
print("Controle:\t\t\t", ctrl)
print("Entrada 1:\t\t\t", in1)
print("Entrada 2:\t\t\t", in2)
print("Temporário:\t\t\t", T1)
print("Saída:\t\t\t\t", T2)
print("Dreno (Primeiro Switch P):\t", D1)
print("Dreno (Segundo Switch P):\t", D2)
