def binary_search(lst1,data):
    n = len(lst1)
    low = 0
    high = n-1
    mid = int((low+high)/2)
    for i in range(n):
        if data == lst1[mid]:
            return mid
        elif data>mid:
            low = mid +1
        elif data<mid:
            high = mid -1
    return -1
    
print(binary_search([1,3,7,9,11],7))
    
