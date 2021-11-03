def binarySearch(arr, n,left, right, x):
   while(left <= right):
     mid = (left + right) // 2
     if(arr[mid] == x):
        return mid+1
     elif(arr[mid] < x):
        left = mid+1
     else:
        right = mid-1
   return -1

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

if(answer == -1):
  print("element not found in the array")
else:
  print("element found at position:",answer)
     
