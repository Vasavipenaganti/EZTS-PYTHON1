'''def isprime(m):
    for i in range(2,m):
        if m%i == 0:
            return "Composite"
    else:
        return "Prime"
n = int(input())
d={}
for i in range(n):
    k = i+1
    v = isprime(i+1)
    d[k]=v
print(d)'''

'''10
{1: 'Prime', 2: 'Prime', 3: 'Prime', 4: 'Composite', 5: 'Prime', 6: 'Composite', 7: 'Prime', 8: 'Composite', 9: 'Composite', 10: 'Composite'}'''

def isprime(m):
    for i in range(2,m):
        if m%i == 0:
            if i%2==0:
                return "even"
            else:
                return "odd"
    else:
        return "Prime"
n = int(input())
d={}
for i in range(n):
    k = i+1
    v = isprime(i+1)
    d[k]=v
print(d)

'''10
{1: 'Prime', 2: 'Prime', 3: 'Prime', 4: 'even', 5: 'Prime', 6: 'even', 7: 'Prime', 8: 'even', 9: 'odd', 10: 'even'}'''


