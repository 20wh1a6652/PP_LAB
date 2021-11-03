
def linearSearch(arr, n, x, i):
  if(i>=n):
    return 0
  elif(arr[i] == x):
    return i+1
  else:
    return linearSearch(arr, n, x, i+1)


n = int(input("enter the size of an array"))
print("enter the array elements")
arr = []
for i in range(0, n):
   ele = int(input())
   arr.append(ele)

x = int(input("enter the search element"))


ans = linearSearch(arr, n, x, 0)

if(ans != 0):
  print("element found at position:",ans)
else:
  print("element not found")
