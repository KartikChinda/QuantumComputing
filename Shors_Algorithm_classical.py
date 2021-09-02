# Picking a composite number and a number a that is co prime with the number:

import math
N = 15
a = 13

# This part is actually used for plotting the graph and finding the period, but we want it to find the value of r for our formula as well.
z = list(range(N))
y = [a**z0 % N for z0 in z]


# Basically, this is what happens. r is the smallest integer in which the value of N%a beins to repeat itself. Thus, we can find the period of the function. And once we get the period of the function, it becomes evident that the two prime numbers must be where the graph starts and where it ends, which precisely is x+1 and x-1. All that is left to do, is find the GCD of the two numbers with N respectively, and those are our values.
r = z[y[1:].index(1)+1]

if r % 2 == 0:
    x = (a**(r/2.)) % N
    print(f'x = {x}')
    if((x+1) % N) != 0:
        print(math.gcd((int(x)+1), N), math.gcd((int(x)-1), N))
    else:
        print("x+1 % N is zero.")
else:
    print(f'r = {r} is odd')
