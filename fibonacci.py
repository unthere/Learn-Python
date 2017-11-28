# Fibonacci

def fib(max):
    n,a,b=0,0,1
    while n < max:
        print b
        b=a+b
        a=b-a
        n=n+1
    return 'done'

print fib(20)
