'''
a = {1,2,3,4}
b = {2,3,4,5}
print(a.union(b))
print(a|b)


{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}'''

'''a = {1,2,3,4}
b = {2,3,4,5}
print(a.intersection(b))            #common elements 
print(a&b)

{2, 3, 4}
{2, 3, 4}'''

'''a = {1,2,3,4}
b = {2,3,4,5}
a.intersection_update(b)     #a updated with intersection elements
print(a)
print(b)

{2, 3, 4}
{2, 3, 4, 5}'''

'''a = {1,2,3,4}
b = {2,3,4,5}
print(a.difference(b))
print(a-b)

{1}
{1}'''

'''a = {1,2,3,4}
b = {2,3,4,5}
a.difference_update(b)
print(a)
print(b)

{1}
{2, 3, 4, 5}'''

'''a = {1,2,3,4}
b = {2,3,4,5}
print(a.symmetric_difference(b))      #xor symbol
print(a^b)

{1, 5}
{1, 5}'''


'''a = {1,2,3,4}
b = {2,3,4,5}
a.symmetric_difference_update(b)
print(a)
print(b)

{1, 5}
{2, 3, 4, 5}'''

'''s1={10,20,30,40}
s2={30,40,50,60}
print(s1.issubset(s2))

False'''

s1={10,20,30,40}
s2={30,40,50,60}
print(s2.issubset(s1))






