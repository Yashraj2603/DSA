def unordered_array(lst1,data):
    for i in range(len(lst1)):
        if lst1[i] == data:
            return i
    return -1
    
print(unordered_array([2,8,5,4,6],4))
