# Sorting a List in Ascending Order
myList = ['d', 'a', 't', 'a', 'g', 'y']
myList.sort()
print(myList)

# Returns:
# ['a', 'a', 'd', 'g', 't', 'y']

# Sorting a List in Ascending Order
myList = ['d', 'a', 't', 'a', 'g', 'y']
myList.sort(reverse=True)
print(myList)

# Returns:
# ['y', 't', 'g', 'd', 'a', 'a']

# Sorting a List with a Custom Function
fruits = ['apple', 'banana', 'grapefruit', 'plum']

def get_last(word):
    return word[-1]

fruits.sort(key=get_last)
print(fruits)

# Returns:
# ['banana', 'apple', 'plum', 'grapefruit']

# Sorting a List of Lists by Their Length
lists = [[1,2,3], [4, 5], [6], [7,8,9, 10]]
lists.sort(key=len)

print(lists)

# Returns:
# [[6], [4, 5], [1, 2, 3], [7, 8, 9, 10]]

# Sorting a List of numbers
nums = [-1,1,-2,3,5]
nums.sort()

print(lists)

# Returns:
# [-2, -1, 1, 3, 5]

# Sorting a List of Dictionaries by a Value
people = [
    {'Name': 'Ali', 'Age': '24', 'City': 'Tehran'}, 
    {'Name': 'Mohammad Javad', 'Age': '24', 'City': 'Dezful'}, 
    {'Name': 'Armin', 'Age': '25', 'City': 'Ahvaz'}]

people.sort(key=lambda x: x.get('Name'))

print(people)

# Returns:
# [{'Name': 'Ali', 'Age': '24', 'City': 'Tehran'},
# {'Name': 'Armin', 'Age': '25', 'City': 'Ahvaz'},
# {'Name': 'Mohammad Javad', 'Age': '24', 'City': 'Dezful'}]
