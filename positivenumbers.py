a=[]
n=int(input("enter the value of n"))
#creating the list
for i in range (n): 
    b=int(input("enter value for array"))
    a.append(b)
#checking for positive numbers in the list
for i in a:
    if(i>=0):
        print(i, end=",")
