def fatorial(num,show=False):
    """Help on function fatorial in module _main_:
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número. 
        :param n: O número a ser calculado. 
        :param show: (opcional) Mostrar ou não a conta. 
        :return: O valor do Fatorial de um número n.
    """
    fatorialnum=1
    while num != 0:
        fatorialnum = fatorialnum*num
        #print("fatorial",fatorialnum," * num",num)
        if show and num != 1:
            print(num, end=' X ')
        num -=1
    if show :
        print(num+1, end=' = ')
    return(fatorialnum)
        
print(fatorial(5,True))
print(fatorial(5))
help(fatorial)