marks1 = 93.6
marks2 = 85.5
marks3 = 90.0
marks4 = 88.2

marks = [93.6, 84.5, 89.3, 44.6]
print(marks)
print(marks[0])
print(type(marks))
# list k anadar hum access kisi ibhi pr aur change kisi bhii value ko kar skte h
str = "hello"
print(str[0])
# str[0] = "H" #not possible

student = ["aman", 21, "dhairya", 87]
print(student[0])
student[0] = "aman kumar"
print(student[0]) #possible in lists
print(marks[1:])
print(marks[-3:-1]) #slicing in list
#list methods
list = [2,1,3] 
list.append(4)
print(list)
#sorting --> ascending and descending
list.sort()
print(list)
list.sort(reverse=True)
print(list)
l1 = ["bag", "at"]
print(l1.sort())
print(l1)
list.reverse() 
list.insert(2,9)
print(list)
list.remove(2)
print(list)
list.pop(2) 
print(list)

# TUPLES - immutable data structure, we cannot change any value in a tuple, we can only access the values
tup = (87, 64, 45, 79, 45, 90)
print(type(tup))
print(tup[0])
t1 = () #--> empty tuple
t2 = (1, ) #  --> tuple with one element, we need to add a comma after the element to create a tuple with one element
print(tup[1:4])
print(tup.index(64))
print(tup.count(45))

m1= input("enter your favourite movie:")
m2= input("enter your favourite movie:")
m3= input("enter your favourite movie:")

list = []
list.append(m1)
list.append(m2)
list.append(m3)
print(list) 

list1 = [1, 2, 1]
copy = list1.copy()
copy.reverse()

if(list1 == copy):
    print("palindrome")
else:
    print("not palindrome")

