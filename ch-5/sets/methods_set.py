d = {1, 4, 56, 4, "muskan"}
d.add(566)
print(d, type(d)) #1, 4, muskan, 566, 56

#properties
#1. sets are unordered
#2. uniindexed -> can't access elements by index
#3. no way to chande items in sets
#4. can't conatin duplicate values
 
print(len(d))
print(d.remove(1))
print(d)
print(d.pop())  #removes randon element
d.clear()  #clear sets
