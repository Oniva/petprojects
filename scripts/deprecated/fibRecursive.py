import timeit

start = 0
def fibonacci(n):
    global start
    if(not(start)):
        start = timeit.default_timer()
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(int(input("Enter Nth Fib Number"))))
print(timeit.default_timer()-start)