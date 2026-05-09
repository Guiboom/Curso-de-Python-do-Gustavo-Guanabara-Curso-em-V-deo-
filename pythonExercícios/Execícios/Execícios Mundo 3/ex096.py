def área(c,l):
    areacalculada = c*l
    return areacalculada

print('-----------Calculo terreno-----------')

comprimento = float(input('Qual o comprimento do terreno?: '))
largura = float(input('Qual a largura do terreno?: '))

print('-'*37)

areacalculada = área(comprimento,largura)

print(f"Um terreno de {comprimento}m de comprimento e {largura}m de largura, tem {areacalculada}m²")