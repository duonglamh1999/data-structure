def binarySearch (arr,left,right,target):
    if left<=right:
        midInd = (right + left)//2
        midVal = arr[midInd]
        if midVal==target:
            return midInd
        elif target<midVal:
            right = midInd-1
            return binarySearch(arr,left,right,target)
        else:
            left = midInd+1
            return binarySearch(arr,left,right,target)
    return -1
def findPivot(arr, left, right):
    if right < left:
        return -1
    mid = (left + right)//2
    if mid < right and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > left and arr[mid] < arr[mid - 1]:
        return (mid-1)
    elif arr[mid]>arr[right]:
        return findPivot(arr,mid+1,right)
    else:
        return findPivot(arr,left,mid-1)
  
def findRotatedIndex (arr,target):
    pivot = findPivot(arr,0,len(arr)-1)
    if target == arr[pivot]:
        return pivot
    elif target<=arr[0]:
        return binarySearch(arr,pivot+1,len(arr)-1,target)
    else: 
        return binarySearch(arr,0,pivot-1,target)

print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4,5], 9))