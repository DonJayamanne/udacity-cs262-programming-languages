# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number



# Try it on your own!
def findmax(f, l):
    sortedL = sorted(l, key=f, reverse = True)
    return sortedL[0]

# Test cases:
l1 = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f1 = len

l2 = [1, 2, 5, -10, 0]
f2 = abs

def lpos(word):
    return word.find('l')
    
print findmax(f1, l1)
print findmax(f2, l2)
print findmax(lpos, l1)
# or use lambda

print findmax(lambda(word): word.find('l'), l1)



