def fib(n=4):
    
    if n <= 0:
        print(-1)
    if n== 1:
        print(0)
    if n == 2:
        print(0,',', 1)
    if n > 2:
        a = 0
        b = 1
        print(0, end=', ')
        print(1, end=', ')
        for i in range(n-2):
            sum = a+b 
            a = b 
            b = sum 
            print(sum, end=', ')

fib(10)