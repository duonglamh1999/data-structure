def countZeroes(arr):
    right = len(arr)-1
    ind = findFirstZero(arr,0,right)
    if ind==-1:
        return 0
    
    return len(arr)-ind 
def findFirstZero(arr,left,right):
    if left<=right:
        midInd = left +(right - left)//2
        midVal = arr[midInd]
        print(f'{arr[left:right+1]}')
        if (midInd==0 or arr[midInd-1]==1) and midVal==0:
            return midInd
        elif midVal==1:
            left = midInd+1
            return findFirstZero(arr,left,right)
        else:
            right = midInd-1
            return findFirstZero(arr,left,right)
    return -1

print(countZeroes([1,1,1,1,1,1,0]))
