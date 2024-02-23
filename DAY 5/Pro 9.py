#To maintain students marks database using nested dictionary
n , m = map(int,input().split())
d = {}
for i in range(n):
    k = input("enter Roll number:")
    v = {}
    for i in range(m):
        k1 = input("enter sub name:")
        v1 = input("enter the marks:")
        v[k1]=v1
    d[k]=v
print(d)
for i in d.items():
    print(i)

'''enter Roll number:485
enter sub name:m1
enter the marks:10
enter sub name:m2
enter the marks:9
enter Roll number:490
enter sub name:m1
enter the marks:10
enter sub name:m2
enter the marks:9
{'485': {'m1': '10', 'm2': '9'}, '490': {'m1': '10', 'm2': '9'}}
('485', {'m1': '10', 'm2': '9'})
('490', {'m1': '10', 'm2': '9'})'''
