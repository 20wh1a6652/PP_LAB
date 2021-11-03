def binarySearch(arr, n,left, right, x):
     mid = (left + right) // 2
     if(left > right):
        return 0
     elif(arr[mid] == x):
        return mid+1
     elif(arr[mid] < x):
        left = mid+1
     elif(arr[mid] > x):
        right = mid-1
     else:
        return binarysearch(arr, n, left, right, x)
     


n = int(input("enter the size of an array"))

print("enter the array elements")
arr = []
for i in range(0, n):
   ele = int(input())
   arr.append(ele)
arr.sort()
print(arr)
x = int(input("enter the search value"))

answer = binarySearch(arr, n, 0, n-1, x)

if(answer != 0):
  print("element found at position:",answer)
else:
  print("element not found in the array")
     
