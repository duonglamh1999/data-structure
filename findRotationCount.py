def countRotation (arr):
    right = len(arr)-1
    res= search(arr,0,right)
    return res
def search(arr,left,right):
    if left<=right:
        mid = (right + left)//2
        print(arr[left:right+1])
        print(mid)
        if arr[mid]>arr[mid+1]:
            return mid+1
        elif arr[mid]<arr[mid-1]:
            return mid
        elif arr[mid]<arr[right]:
            right = mid-1
            return search(arr,left,right)
        else:
            left = mid+1
            return search(arr,left,right)
print(countRotation([13,14,15, 18,12]))