#To maintain students marks database using nested dictionary
n , m = map(int,input().split())
d = {}
for i in range(n):
    k = input("enter Roll number:")
    v = {}
    for i in range(m):
        k1 = input("enter sub name:")
        v1 = int(input("enter the marks:"))
        v[k1]=v1 
    d[k]=v
for i in d:
    l = list(d[i].values())
    print(f"{i} : {sum(l)/m}")

'''enter Roll number:490
enter sub name:2
enter the marks:10
enter sub name:m2
enter the marks:98
enter Roll number:485
enter sub name:m1
enter the marks:90
enter sub name:m2
enter the marks:46
490 : 54.0
485 : 68.0'''

'''n , m = map(int,input().split())
d = {}
for i in range(n):
    k = input("enter Roll number:")
    v = {}
    avg=0
    for i in range(m):
        k1 = input("enter sub name:")
        v1 = int(input("enter the marks:"))
        v[k1]=v1
        avg +=v1 
    d[k]=v
print(d)
print("Average:",avg/m)'''

'''1 2
enter Roll number:85
enter sub name:m1
enter the marks:3
enter sub name:m2
enter the marks:3
{'85': {'m1': 3, 'm2': 3}}
3.0'''
