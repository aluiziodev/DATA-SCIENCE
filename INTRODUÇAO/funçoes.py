def imprime(n):
    print(n)

def potencia(n):
    return n*n

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#print(fib(int(input())))

def intervalo(i= 0, f = 10):
    for j in range(i, f+1):
        print(j)

intervalo()
intervalo(2, 8)




