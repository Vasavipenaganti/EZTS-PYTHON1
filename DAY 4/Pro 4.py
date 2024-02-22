'''t = (21,51,32,32,51,51,10)
print(t.count(t[t.index(51)+1]))                   #2'''

#To print sum max n min elements in a matrix using tuple
r,c = int(input()),int(input())
l = []
for i in range(r):
    l.append(tuple(map(int,input().split())))
max,min=0,1000
for i in l:                 #i= tuple
    print(i)
    for j in i:             #j = element in tuple
        if j>max:
            max = j
        if j < min:
            min = j
print(max+min)

'''3 
3
1 3 4
43 87 4
99 3 2
(1, 3, 4)
(43, 87, 4)
(99, 3, 2)
100'''
            
    
    
#To print tuple matrix
'''r,c = int(input()),int(input())
l = []
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    print(i)'''

'''3
3
1 2 3
4 5 6
7 8 9
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)'''
