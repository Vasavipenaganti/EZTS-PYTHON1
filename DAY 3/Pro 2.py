#comparing the 2 strings and print the count of different letters and same letters
'''s = input()
s1 = "codeforces"
c=0
for i in range (len(s)):
    if s[i] != s1[i]:
        c+=1
print(c)'''
        
'''coolforces
2
cadafurcle
5
codeforces
0'''

s = input()
s1 = "codeforces"
c=0
for i in range (len(s)):
    if s[i] == s1[i]:
        c+=1
print(c)

'''coolforces
8'''

