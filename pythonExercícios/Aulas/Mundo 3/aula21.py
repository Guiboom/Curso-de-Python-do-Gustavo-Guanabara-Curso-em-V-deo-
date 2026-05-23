#1
#terminal: 
#python
#help()
#EX para ver uma biblioteca:
# datetime
#quit

#no codigo tambem help(X)
#X=Sem aspas: Tipos (str, list), funções (print, len), métodos (list.append) e módulos importados.
#Com aspas: Comandos estruturais ("if", "for", "def") e listas globais do Python ("TOPICS", "MODULES").
#EX:
#help(print)
#print(input.__doc__)

#2
def contador(i,f,p):
    """-> Faz uma contagem a mostra na tala.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        """
    c=i
    while c<=f:
        print(f'{c}',end='..')
        c+=p
    print("FIM")

#help(contador)

#3
def somar(a=0,b=0,c=0):#abc se torna opcional
    s=a+b+c
    print(f"A soma vale {s}")

somar(3,2,5)
somar(3,2)
somar(b=3,c=2)
somar()

#4
def teste():
    global p #quando faz isso ele consegue uma variavel de fora e altera a mesma
    x=2
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")
    print(f"Na função teste, p vale {p}")

#programa principal
n=2
p=5
print(f"Na função teste, n vale {n}")#Funciona pois "n" existe em todo o codigo("Não foi criado dentro de uma função")
teste()
#print(f"Na função teste, x vale {x}")#Não funciona pois "x" só existe dentro da função
print(f"Na função teste, p vale {p}")


#5
def somar2(a=0,b=0,c=0):#abc se torna opcional
    s=a+b+c
    return s

resp = somar2(3,2,5) #resp passa a ter o mesmo valor de s