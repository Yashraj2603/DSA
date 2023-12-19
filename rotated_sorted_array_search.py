'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def bin_search(low,high,lst1,data):
    n = len(lst1)
    mid =int(low+(high-low)/2)
    if low>=high:
        return -1 
    elif lst1[mid]== data:
        return mid
    elif lst1[mid]>data:
        return bin_search(low,mid-1,lst1,data)
    else:
        return bin_search(mid+1,high, lst1,data)
def find_pivot(a,low,high):
    mid = int(low +(high-low)/2)
    if low > high:
        return -1
    elif (low<high and a[mid]<a[mid+1]):
        return mid + 1 
    elif mid>low and a[mid-1] > a[mid]:
        return mid
    elif a[low]<a[mid]:
        return find_pivot(a,mid+1 ,high)
    else:
        return find_pivot(a,low,mid-1)
        
def find_key(a,n,key):
    pivot = find_pivot(a,0,n-1)
    if pivot == -1:
        return(bin_search(0,n-1,a,key))
    elif a[pivot] == key:
        return pivot
    elif a[0]>key:
        return bin_search(0,pivot-1,a,key)
    else:
        return bin_search(pivot+1,n-1,a,key)
        
        
        
a = [50, 60, 70, 80, 90, 10, 20, 30, 40]
n = len(a)
key = 30

result = find_key(a, n, key)
print(result)
