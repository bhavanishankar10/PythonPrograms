# Variables , DataTypes concept

print("Hello world in Python")

a = 100
b = 120
print("Output = " , a+b) # both are same datType of int - so get output 

a = "100"
b = 120
#print("Output = " , a + b) error - typeError for a+b - string can only concatenate with strings not int dataType
print("Type of a = " ,type(a) ," and ", "Type of b = " , type(b))

a,b,c = 10,20,30  #assigning many values to multiple variables
print(a,b,c)

a=b=c="apple"  #assigning 1 value to multiple variables
print(a,b,c)


x = "awesome"   # global variable
def myFunc():
    # global x   -> here we are making a local variable into a global variable using "global" keyword
    # x = "fantastic"
    x = "fantastic"     #local variable
    print("Python is " + x)
myFunc()
print("Python is " + x)

# making changes in file to observe how git works 
print("--- Changes Made -> This was 2nd commit by the way---")
# now making a 3rd commit
print("This was 3rd commit")