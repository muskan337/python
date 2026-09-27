s1 = {1, 45, 6}
s2 = {7, 8, 1, 78, 45}

print(s1.union(s2)) #combines the values of both s1 and s2 with no repeated values
print(s1.intersection(s2)) #common values between s1 and s2

print(s1-s2) #6

s = {1, 2, 3}
s.update([4, 5, 6])

print(s)


s = {10, 20, 30, 40}
s.remove(30) #removes an element and also gives an error if elements not present

print(s)


s = {10, 20, 30}
s.discard(50) #removes an element but does not give an erroe if elements not present

print(s)


s = {10, 20, 30}

x = s.pop() #removes and returns an arbitrary element

print(x)
print(s)   


s1 = {1, 2, 3, 4}

s1.clear() #removes all elements from the set

print(s1)

s3 = s.copy()
print(s3)

A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
print(A.issuperset(B))

C = {1, 2, 3}
D = {4, 5, 6}

print(C.isdisjoint(D)) #to check whether two sets has no common elements