# numbers = [1, 7, 0, 4, 0, 5, 6, 0, 3]
# new_list = [num for num in numbers if num != 0] + [num for num in numbers if num == 0] + [num.sort() for num in numbers if num ==0]
# print(new_list)
def pushZerosToEnd(arr, n):
    count=0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
for ar in arr:
    if ar != 0:
        arr.sort()
n = len(arr)
pushZerosToEnd(arr, n)


print("Array after sorting and pushing all zeros to end of array:")
print(arr)