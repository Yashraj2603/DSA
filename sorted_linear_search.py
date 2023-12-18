def sorted_linear(lst1,data):
    for i in range(len(lst1)):
        if lst1[i] == data:
            return i
        elif lst1[i]>data:
            return -1
    return -1
    
print(sorted_linear([1,3,8,9],8))
