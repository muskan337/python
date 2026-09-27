s = set()
s.add(20)
s.add(20.0) #floating and integers are considered same in sets
s.add('20') 

print(s)
print(len(s))