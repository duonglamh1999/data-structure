def findFloor(arr,target):
    return
def search(arr,left,right,target):
    if left<=right:
        midInd = (right + left)//2
        midVal = arr[midInd]
        if midVal==target:
            return midInd
        elif midInd>0 and target<midVal and target>arr[midInd-1]:
            return midInd-1
        elif target<midVal:
            right = midInd-1
            return search(arr,left,right,target)
        else:
            left = midInd+1
            return search(arr,left,right,target)
    return -1