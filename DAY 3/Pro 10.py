#strong number using recursion and strings
'''def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s = str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum == x:
        return "strong Number"
    else:
        return "Not a Strong Number"
    
x = int(input())
print(strong(x))'''

'''145
strong Number
89
Not a Strong Number'''

#strong number in a range
def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s = str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum == x:
        print(x)
a,b = int(input()),int(input())
for i in range (a,b+1):
    strong(i)
print(strong(i))

'''100
1000000
>>145
40585
None'''

