def getFirst(arr,left,right,n):
    if left<=right:
        midInd = (right + left)//2
        midVal = arr[midInd]
        if (midInd==0 or n>arr[midInd-1]) and midVal==n:
            return midInd
        elif midVal<n:
            left = midInd+1
            return getFirst(arr,left,right,n)
        else:
            right = midInd-1
            return getFirst(arr,left,right,n)
    return -1

def getLast(arr,left,right,n):
    if left<=right:
        midInd = (right + left)//2
        midVal = arr[midInd]
        if (midInd==(len(arr)-1) or n<arr[midInd+1]) and midVal==n:
            return midInd
        elif n<midVal:
            right = midInd-1
            return getLast(arr,left,right,n)
        else:
            left = midInd+1
            return getLast(arr,left,right,n)
    return -1
def sortedFrequency (arr,n):
    left = 0
    right = len(arr)-1
    first = getFirst(arr,left,right,n)
    if first ==-1:
        return 0
    last = getLast(arr,left,right,n)
    return last-first+1 

# print(sortedFrequency([1,1,2,2,2,2,3],1))
print(sortedFrequency([1,1,2,2,2,2,2,2],2))