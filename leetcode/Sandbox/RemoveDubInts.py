List = [0,0,1,1,1,2,2,3,3,4,4,4,4]
List2 = [0,1,2]

def removeDub(x):
    item = 0
    index = item + 1


    while index <= len(x):

        if item < len(x) and index < len(x):
            if x[item] == x[index]:
                print(x[index])
                del x[index]
            else:
                item += 1
                index = item + 1
        else:
            break

    print(x)

    return len(x)


print(removeDub(List2))
