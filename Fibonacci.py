#This codes shows how to calculate a Fibonacci number using 3 approaches 

import time # to calculate running time 

#Using Recursion 
def fib_recusion(x):
    if (x == 1) or (x == 2):
        return 1
    return fib_recusion(x-1) + fib_recusion(x-2)
    
    
#Using dynamic programing - memoization 
def fib(x, mem):
    if mem[x] != None:
        return mem[x]
    if (x == 1) or (x == 2):
        result = 1
    else:
        result = fib(x-1, mem) + fib(x-2, mem)

    mem[x] = result
    return result

def fib_mem(x):
    mem = [None] * (x+1)
    return fib(x, mem)
    
#print results and compare time 
start_time = time.time()
fib_recusion(11)
print("Recursion took: --- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
fib_mem(11)
print("DP took: --- %s seconds ---" % (time.time() - start_time))
