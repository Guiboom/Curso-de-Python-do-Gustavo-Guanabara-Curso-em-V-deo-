import math
ang = float(input('Digite quantos graus tem o ângulo: '))
raio = math.radians(ang)
seno = math.sin(raio)
cosseno = math.cos(raio)
Tangente = math.tan(raio)
print(f'Seno: {seno:.3f45}')
print(f'Cosseno: {cosseno:.3f}')
print(f'Tangente: {Tangente:.3f}')