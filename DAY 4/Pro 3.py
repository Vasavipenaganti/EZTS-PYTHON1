#To print product of the matrix
row,column = int(input()),int(input())
l=[]                      #l is empty so we use append
for i in range(row):
    l.append(list(map(int,input().split())))
#print(l)
p = 1
for i in l:
    print(i)
    for j in i:
        p*=j
print(p)
    


'''3
3
1 2 3
4 5 6
7 8 9
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
362880'''


#Without using append function
row,column = int(input()),int(input())
l=[0]              #0 is in l so l is not empty list we didn't use append
for i in range(row):
    l[i]=list(map(int,input().split()))
#print(l)
p = 1
for i in l:
    print(i)
    for j in i:
        p*=j
print(p)

'''2
2
1 2
1 2
[1, 2]
[1, 2]
4'''
    
