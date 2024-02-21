#To make encryption and decryption with a key value using functions
def encryption(s,k):
    v = ""
    for i in s:
        temp=ord(i)+k
        chr(temp)
        v+=chr(temp)
    print(v)
def decryption(s,k):
    v=""
    for i in s:
        temp=ord(i)-k
        chr(temp)
        v+=chr(temp)
    print(v)
k = int(input("Enter key value: "))
s = input("Enter string: ")
op = input("Enter the operation: ")
if op=="encryption":
    encryption(s,k)
elif op=="decryption":
    decryption(s,k)
else:
    print("Inproper operation")

'''Enter key value: 4
Enter string: vasavi
Enter the operation: encryption
zewezm

Enter key value: 4
Enter string: vasavi
Enter the operation: decryption
r]o]re

Enter key value: 6
Enter string: vasavi
Enter the operation: encryption
|gyg|o'''
    
        
#To print ascii values of given string
'''def enc(n):
    for i in n:
        ord(i)
        print(ord(i))
n = input()
enc(n)'''
