def factorial(n):
    if n==0:  #base case
        return 1
    else:   #recursive case
        return n*factorial(n-1)

print(factorial(5))
