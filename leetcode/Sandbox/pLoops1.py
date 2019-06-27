myArray = [5,2,73,4,14]

for i in range(len(myArray)):
    print("In loop 1 ", i)
    for j in range(i+1, len(myArray), 1):
        print("In loop 2 ", j)
