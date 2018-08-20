import timeit

try:
    def fibonacci(n):
        start = timeit.default_timer()
        if n == 1 or n == 2:
            return 1
        fibList = [None] * (n+1)
        fibList[1] = 1
        fibList[2] = 1
        for i in range(3, n+1):
            fibList[i] = fibList[i-1] + fibList[i-2]
        stop = timeit.default_timer()
        print(stop-start)
        return fibList[n]
except KeyboardInterrupt:
    print("k bai")
    

print(fibonacci(int(input("Enter Nth Fib Number: "))))