# if-elif-else ladder
a = int(input("Enter your age: "))

if(a>=18):
    print("your are above the age of consent")
    print("good for u")

elif(a<0):
    print("You are entering an invalid age")

elif(a == 0):
    print("a is not a valid age")

else:
    print("You are below the age of consent")

print("end of program")

#indent- empty space in elif, if, else statement