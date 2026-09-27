''''
factorial(5) = 5*4*3*2*15

factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(n) = n X n-1 X n-2X ......X 2 X 1

'''
def factorial(n):
    if(n==0 or n == 1):
        return 1
    return n*factorial(n-1)

n = int(input("Enter the nnumber n: " ))

print(f"The factorial of this number is: {factorial(n)}")