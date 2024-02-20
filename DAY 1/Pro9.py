#write a python program is to check year is leap year are not?
#if year divide by 400 is a leap year elif year divide by 4 and year not divide by 100 print leap year
y=int(input())
if y%400==0 or (y%4==0 and y%100!=0):
    print("Leap Year")
else:
    print("Not a Leap year")
