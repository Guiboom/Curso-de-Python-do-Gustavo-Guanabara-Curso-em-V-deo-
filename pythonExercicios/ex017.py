import math
catAdj = float(input('Digite o comprimento do cateto adjacente: '))
catOpo = float(input('Digite o comprimento do cateto oposto: '))
hipot = math.hypot(catOpo,catAdj)
print(f'A hipotenusa é:{hipot}')