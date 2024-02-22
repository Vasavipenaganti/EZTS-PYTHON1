# To print avearge of the  matrix
r,c = int(input()),int(input())
l,sum = [],0
for i in range (r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
        sum+=j
print(sum/(r*c))

'''
>>>2
>>>2
>>>1 2
>>>3 4
2.5'''

