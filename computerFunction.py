def computerFunction(a,b):
    return a^b


#print(computerFunction(61,233))

x, y = [int(x) for x in input("Enter two value (space): ").split()]
computerFunc = computerFunction(x,y)
print(computerFunc)