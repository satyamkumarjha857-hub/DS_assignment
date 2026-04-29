
# RECURSSIVE FACTORIAL

# BASE CASE : SIMPLEST PROBLEM THAT RETURNS ANSWER DIRECTLY
# RECURSSIVE CASE : PROBLEM SOLVED BY CALLING ITSELF WITH SMALLER INPUT
# STACK GROWTH : EACH RECURSSIVE CALL ADDS TO STACK FRAME

def factorial(n): # function defination

    if n<0:  # handling the negative inputs
        print("Please Enter a positive number !")
        return None
    
    elif n==0 or n==1:   # base case
        return 1
    
    else:  # recurssive case
        return n*factorial(n-1)

print("Factorial :")    

# calling the function and taking an input from the user
print(factorial(int(input("Enter any number :"))))  









