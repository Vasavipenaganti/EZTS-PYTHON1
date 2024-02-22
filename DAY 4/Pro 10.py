#To print word,count of vowels,list of a vowels each word in a sentence using functions
def sen(n):
    print(n)
    s=""
    for i in n:
        print(i)
        for j in i:
            if j in "aeiouAEIOU":
                s+=i
    print(list(set(s)))
n = map(str,input().split())
sen(n)


    

    
    
