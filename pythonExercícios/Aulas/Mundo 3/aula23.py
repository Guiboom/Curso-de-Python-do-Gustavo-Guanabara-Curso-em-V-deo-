#erro de sintaxe:

#primt(x)


#erro de significado pois n tem valor o x

#print(x)


#erro de exceção

#n = int(input('Número: '))

#usuário digite: oito

#outro erro de exceção

#a=8
#b=0
#r=a/b

#use o try e except

try: #tente isso
    a=int(input('Digite um número: '))
    b=int(input('Digite outro número: '))
    r = a/b
except Exception as erro: #Caso falhe
    print('Infelizmente tivemos um problema :(')
    print(erro.__class__)
    
else:
        print(f"{a} / {b} = {r}")
        
finally:
    print('Volte sempre!')