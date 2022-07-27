import re


def findFloor(arr,target):
    res = search(arr,0,len(arr)-1,target)
    return res
def search(arr,left,right,target):
    if left<=right:
        mid = (right + left)//2
        print(f"{arr[left:right+1]} mid:{arr[mid]} target:{target}")
        if arr[mid]==target:
            return mid
        elif arr[right]< target:
            return arr[right]
        elif mid>0 and target<arr[mid] and target>arr[mid-1]:
            return mid-1
        elif target<arr[mid]:
            right = mid-1
            return search(arr,left,right,target)
        else:
            left = mid+1
            return search(arr,left,right,target)
    return -1
print(findFloor([1,2,8,10,10,12,19], 20)) 