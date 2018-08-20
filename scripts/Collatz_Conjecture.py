
#! python 3
import sys

count = 0
def collatz(n):
    global count
    if n == 1:
        print(count)
    elif n % 2 == 0:
        count += 1 
        collatz(n / 2)
    else:
        count +=1 
        collatz(n * 3 + 1)

collatz(int(sys.argv[1]))