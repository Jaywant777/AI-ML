# issuperset()
# issubset()
# isdisjoint()

# s1,s2={1,2,3,4,5,6,7,8,9},{5,6,7,8,9}
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))




# s={1,2,3,4,'python','java'}

# Copy
# ss=s.copy()
# print(s)

# # clear
# # s.clear()
# # print(s)

# s.add('php')
# print(s)

# # update,hold unique element in it.
# s.update({6,5,4,3})
# print(s)

# #  pop,remove random element in set.
# # print(s.pop())

# # remove
# s.remove('python')
# print(s)

# s.discard('hello')
# print(s)


# frozenset,is unique element

# f='python'
# l=[10,20,30,'python']
# t=[1,2,3,4,'python']

# fs1=frozenset(f)
# print(fs1,type(fs1))

# fs2=frozenset(l)
# print(fs2,type(fs2))

# fs3=frozenset(t)
# print(fs3,type(fs3))

# perform id,type,min,MAX,MIN



# This one is diffrent
fs1=frozenset({1,2,3,4,5})
fs2=frozenset({4,5,6,7,8})

# union
print(fs1.union(fs2))

# intersection
print(fs1.intersection(fs2))

# diffrence
print(fs1.difference(fs2))

# symmetric_difference
print(fs1.symmetric_difference(fs2))

# isdisjoint
print(fs1.isdisjoint(fs2))

# issubset
print(fs1.issubset(fs2))

# issuperset
print(fs1.issuperset(fs2))

# learn complete datatype
# Fundamental is completed.
# Next is control statement.