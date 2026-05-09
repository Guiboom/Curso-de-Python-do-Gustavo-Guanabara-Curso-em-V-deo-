# def lin():
#    print("-------------")

# def titulo(msg):
#    print("-"*(len(msg)+4))
#    print(' ',msg,' ')
#    print("-"*(len(msg)+4))

# print("-------------")
# print("     Olá     ")
# lin()
# titulo('Me chamo Guilherme')


def soma(a, b):
    s = a + b
    print(s)

def somavarios(* núm):
    s=0
    for valor in núm:
        s += valor
    print(s)

def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1


valores=[0,1,2,3,4,5,6,7,8,9,10]

a = 4
b = 5
s = a + b
print(s)

soma(8,9)

soma(b=2,a=1)

somavarios(1,2,6,32,2,34,65,7,6)

print(valores)
dobra(valores)
print(valores)
dobra(valores)
print(valores)
dobra(valores)
print(valores)




