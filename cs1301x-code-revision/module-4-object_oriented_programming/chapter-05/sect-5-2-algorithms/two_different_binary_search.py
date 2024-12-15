

def looping_binary_search(searchList, searchTerm):
    searchList.sort()
    min = 0
    max = len(searchList) - 1
    
    while min <= max:
        currentMiddle = (min + max) // 2
        if searchList[currentMiddle] == searchTerm:
            return True
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1
        else:
            min = currentMiddle + 1
            
    return False



def recursive_binary_search(searchList, searchTerm):
    searchList.sort()

    if len(searchList) == 0:
        return False

    middle = len(searchList) // 2
    
    if searchList[middle] == searchTerm:
        return True
    elif searchTerm < searchList[middle]:
        return binary_search(searchList[:middle], searchTerm)
    else:
        return binary_search(searchList[middle + 1:], searchTerm)
    

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist (looping):", looping_binary_search(intlist, 23))
print("50 is in intlist (looping):", looping_binary_search(intlist, 50))
print("23 is in intlist (recursive):", recursive_binary_search(intlist, 23))
print("50 is in intlist (recursive):", recursive_binary_search(intlist, 50))


