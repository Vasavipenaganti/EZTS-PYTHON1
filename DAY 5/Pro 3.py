n , m = map(int,input().split())
d = {}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())
        if d[i] == v1[:-1]:
            print(f"{k1} {v1} #{i}")

'''2 2
google 2.3.4
utube 5.6.7
insta 5.6.7;
snap 2.3.4;

insta 5.6.7; #utube
snap 2.3.4; #google'''
