#Write a python program to take dictiionary print the keys and values
'''n = int(input("enter the items: "))
d = {}
for i in range (n):
    key = input("key: ")
    value = input("value: ")
    d[key] = value
print(d)'''

'''enter the items: 3
key: 1
value: hi
key: 2
value: hlo
key: 3
value: bye
{'1': 'hi', '2': 'hlo', '3': 'bye'}'''

n = int(input("enter the items: "))
d = {}
for i in range (n):
    key = input("key: ")
    value = input("value: ")
    d[key] = value
for i in d:
    print("key:",i,"values:",d[i])
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)

'''enter the items: 3
key: 1
value: hi
key: 2
value: hlo
key: 3
value: bye
key: 1 values: hi
key:1 value:hi
key:1 value:hi
key: 2 values: hlo
key:2 value:hlo
key:2 value:hlo
key: 3 values: bye
key:3 value:bye
key:3 value:bye
1
2
3
hi
hlo
bye'''



