# Loops
    # while Loops

    # eg 1
i = 1           #initialize
while i < 6:   #condition check
  print(i)
  i += 1        #increment -> if not mentioned -> leads to infinite loop

print("\n")
    # eg 2
i = 1
while i<6 :
    print(i)
    if i==3:
        break   # break example
    i+=1

print("\n")
    # eg 3
i = 0
while i<10:
    i+=1
    if(i==7):
        continue    # continue example
    print(i)

print("\n")
    # eg 4
i = 1           # i=2 -> even nums
print("Odd numbers :")         
while i<20:     # while loop to print odd nums
    print(i,end=' ')
    i+=2
print("\n")
x = range(1,20,2)   # range(2,20,2) -> even nums
print("Odd numbers :")
for i in x:         # for loop to print odd nums
    print(i,end=' ')

print("\n")
    # eg 5
num = 1
while num<13:
    if num%2==0:
        print("Number "+str(num)+" is even")
    else:
        print("Number "+str(num)+" is odd")
    num+=1

