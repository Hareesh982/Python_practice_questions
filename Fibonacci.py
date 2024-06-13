
n = 10
def fibonacci(n):
    fib = [0,1]
    while True:
        if len(fib) == n:
            break
        else:
            fib.append(fib[-1] + fib[-2])
    return fib
    
print(fibonacci(10))


(OR)


n1 = 0
n2 = 1

fib = 7
for i in range(7):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
