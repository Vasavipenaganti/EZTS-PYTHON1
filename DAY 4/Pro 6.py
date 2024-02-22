#To print sum elements in last column of a matrix
r,c=int(input()),int(input())
l,sum = [],0
for i in range(r):         #r is consider, c is not consider
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)


'''
>>>2
>>>2
>>>1 2
>>>1 2
4'''

#To print sum elements in last row of a matrix
''''r,c=int(input()),int(input())
l = []
for i in range(r):         #r is consider, c is not consider
    l.append(tuple(map(int,input().split())))
print(sum(l[-1]))'''
