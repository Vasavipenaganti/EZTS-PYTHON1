'''n = int(input())
d = {}
for i in range(n):
    key,value = map(str,input().split())
    d[key]= value
for i in range(n):
    s = input()
    if s in d:
        print(s,d[s])
    else:
        print("Not Found")'''

'''
>>3
>>sam 45678
>>tom 98765
>>harry 5678765
>>sam
sam 45678
>>eward
Not Found
>>harry
harry 5678765'''

n = int(input())
d = {}
for i in range(n):
    key,value = map(str,input().split())
    d[key]= value
m = int(input("enter the no of items: "))
for i in range(m):
    s = input()
    if s in d:
        print(s,'=',d[s])
    else:
        print("Not Found")

'''
>>3
>>sam 45678
>>tom 98765
>>harry 5678765
>>enter the no of items: 3
>>sam
sam 45678
>>hello
Not Found
>>mi
Not Found'''

