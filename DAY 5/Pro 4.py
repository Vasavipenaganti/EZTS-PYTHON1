#Anagram using string
'''s = input()
s1 = input()
if len(s) == len(s1) and sorted(list(s1)) == sorted(list(s)):
    print("True")
else:
    print("False")'''

'''stop
post
True'''
stop 
#Anagram using dict
d = {}
for i in range(2):
    k,v = map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(l[0]) == len(l[1]) and sorted(list(l[0])) == sorted(list(l[1])):
    print("True")
else:
    print("False")
       
    
            
    
         
