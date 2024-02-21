#To print a n natural numbers using recursion using  stack memory
'''def printing(n):
    if n <1:
        return 1
    else:
        print(n)             
        printing(n-1)    #recursion 
n = 10
printing(n)'''

'''10
9
8
7
6
5
4
3
2
1'''

def printing(n):
    if n <1:
        return 1
    else:
        printing(n-1)
        print(n)
n = 10
printing(n)

'''1
2
3
4
5
6
7
8
9
10'''

