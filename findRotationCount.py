def countRotation (arr):
    left = 0
    right = arr[len(arr)-1]
    return 
def search(arr,left,right):
    if left<=right:
        mid = (right + left)//2
        print(arr[left:right+1])
        print(arr[mid])
        if arr[mid]>arr[mid+1] and arr[mid]<arr[mid-1]:
            return mid
        elif arr[mid]<arr[left]:
            right = mid+1
            return search(arr,left,right)
        else:
            left = mid+1
            return search(arr,left,right)