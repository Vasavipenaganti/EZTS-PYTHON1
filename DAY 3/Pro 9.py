#To print factorial of a given number using recursion
def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input())
print(fact(n))
        
'''5
120'''

