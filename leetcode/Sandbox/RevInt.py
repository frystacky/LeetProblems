number = -201

def reverse(x):
    isNeg = False

    if x<0:
        isNeg = True
        x = x * -1
    print(isNeg)
    print(x)
    print(type(x))

    oldNum = x
    newNum = 0
    modNum = 0
    print(oldNum)

    while oldNum != 0:
        modNum = oldNum % 10
        print(modNum)
        oldNum = int(oldNum/10)
        print(oldNum)
        newNum = (newNum * 10) + modNum
        print(newNum)

    if isNeg:
        newNum = newNum * -1
    return newNum

print(reverse(number))


    
