# simple application of generators in python

# a function for squaring list items
def listSquare(n):
    "enter end of the list as n"
    for i in range(n):
        yield i**2
        
# using listSquare()
ans = listSquare(10)
print(ans)
# returns
# <generator object listSquare at 0x00000197215313C0>

# the ans is a generator object so we can not see it as a list without
# converting it to a list.
ans_in_memory = list(ans)
print(ans_in_memory)
# returns
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# next function for iterating over generators
data = listSquare(3)
next(data)
# returns 0
next(data)
# returns 1
next(data)
# returns 4
