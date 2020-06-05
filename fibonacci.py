Num = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
i = 0
First_Val = 0
Second_Val = 1
           
# Displaying Fibonacci series using while loop
while(i < Num):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Val + Second_Val
                      First_Val = Second_Val
                      Second_Val = Next
           print(Next)
           i = i + 1
