#To Print  matrix using list
'''row,column = int(input()),int(input())
l=[]
for i in range(column):
    l.append(list(map(int,input().split())))
print(l)'''


'''3
3
1 2 3
4 5 6
7 8 9
>>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

#To print sum of the matrix
row,column = int(input()),int(input())
l=[]
for i in range(column):
    l.append(list(map(int,input().split())))
#print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)

'''
>>>3
>>>3
>>>1 2 3
>>>4 5 6
>>>7 8 9
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
45'''

