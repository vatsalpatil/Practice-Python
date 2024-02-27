
def ListPrinter(data):
#     for i, element in enumerate(data):
#         print("Element %d: %s" % (i, element))
    for i, element in enumerate(data):
        print(f'({i+1}) '+f'{element}')

# # Example usage: print out the elements of a list one at a time.
numbers = [5, 23, 76, 49]
ListPrinter(numbers)

a= 0
b= 1
print("Number of iterations %d: %s" %(a,b), end="")