def reversed_list():
    return r[::-1]


r=list(range(0, 11, 2))

print(r)

r = reversed_list()
print(r)

#This is a thought experiment about how to reverse a list without the built-in reverse() method function. The below syntax is with the built in and is the simplest approach but often we use these functions without understanding how they work or other work arounds without them.

#The reversed_list() function works as a method of slicing, where the start and stop args are empty, meaning for the whole list to be iterated through, and the step is -1 which means it will iterate through in reverse and return the reversed list either to the original variable as was done in this example, or to a new variable. 

#this is the built in and simplest way to reverse a list but there are always multiple approachs, and the built in methods may not always be the least resource intensive or efficient in O time.
print(' ')
l=list(range(0, 11, 2))
print(l)
l.reverse()
print(l)
