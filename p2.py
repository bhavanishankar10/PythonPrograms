# String  Concepts


name = "elon musk"   # String -> array ; string characters are indexed from 0,1,2 ....n
print(name[2],"\n")      # variable_name[] helps to get a specific character from string

#for x in name:
    #print(x)

print("length of name = ", len(name))  # length of string

print("Musk" in name) # in checks for specific phrase/char in string "musk"->TRUE, "Musk"->FALSE -                          case senisitve

a = "slicing string"    # String Slicing 
print(a[6:13])
print(a[1:])    # Slicing to the End
print(a[:10])   # SLicing from Start

replaceString = "ran inside"    # .replace() useed to replace a specified string
print(replaceString.replace("n","l"))

print(replaceString.split(" "))   # .split() returns a string as a List of items, items ->separated by separator


    # format strings -> to concatenate strings & number
# eg1
age = 18
name = "rahul"
details = name + " is {} years old"     # {} -> placeholder
print(details.format(age))      # var_name.format() -> combines number & string with help of {}placeholder

# eg2
bats = 5
balls = 8
glove_pair = 7
shop = "There are {2} bats , {1} balls & {0} glovePairs available in shop ." #{} can hold index num as well
print(shop.format(bats,balls,glove_pair))