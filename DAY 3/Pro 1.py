#To Print the smallest vowel repeating odd number of times in a given string
s = input()
s1=""
for i in s:                                           #iteration 
    if i in "AEIOUaeiou":                  #seperation
        if s.count(i)%2!=0:                   #to check odd postion
            s1+=i                                   #append 
print(min(s1))                                  #to print minimum value          
        

'''n = input()
n1 = ""
for i in n:
    if i not in "aeiouAEIOU":
        if n.count(i)%2==0:
            n1+=i
print(min(n1))'''
    
