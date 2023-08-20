# Loops 
    # for Loops

    #eg1
for x in "python":  # for var in sequence(list,tiple,range)
    print(x)

print("\n")
    #eg2
values = range(5)       # range -> buity-in function
for i in values:
    print(i)

print("\n")
    #eg3
items = ["apple","banana","chiku"]      # accessing items of list
for i in items:
    print(i)

print("\n")
    #eg 4.1
digits=[1,2,3,4,5]
for i in digits:
    print(i)
else:
    print("no digits left")
    #eg 4.2
print("\n")
digits = [1,2,3,4,5,6]
for i in digits:
    if i==5:break   # break will stop execution after condition is met
    print(i)
else:
    print("no digits left")

print("\n")
    #eg 5  Nested Loops
list1 = [1,2]
list2 = [3,4]
for i in list1:
    for j in list2: # inner loop will execute 1 time for each iteration of outer loop
        print(i,j)

print("\n")
    #eg 6
for x in range(0,12,2):     #range(start,stop,step)
    print(x,end=' ')

print("\n")
    #eg 7
    # continue keyword
for x in range(1,10):
    if x==8:
        continue
    else:
        print(x,end=' ')

print("\n")
    # eg 8
num = [1,3,2,4,7,9]
maxValue = max(num)     # max() -> gives max value in list
even_count,odd_count=0,0    # set count=0 since we don't know how many are even/odd
for num in num:
    if num%2==0:
        even_count+=1
        print("The number "+str(num)+" is even")
    else:
        odd_count+=1
        print("The number "+str(num)+" is odd")
print("Even nums in list = " , even_count)
print("Odd nums in list = ",odd_count)
print("Max value in list = " ,maxValue)