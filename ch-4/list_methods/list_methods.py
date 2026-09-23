friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
#LISTS PR KOI METHODS USE KROGE TO LIST CHANGE HO JAAYEGI BUT IN CASE OF STRING NO CHANGE IN ORIGINAL STRING

friends.append("me") #append me at the end of the list

print(friends)

l1 = [1, 5, 4, 532, 234, 78]
l1.sort()  #sort the list
print(l1)

l1.reverse() #reverses the list
print(l1)

l1.insert(3, 33333) #(idx, object) insert 33333 at the idx 3
print(l1)

l1.pop(3)  #removes 33333
print(l1)