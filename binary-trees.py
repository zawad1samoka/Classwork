numbers = [1, 2, 3, 4, 5, 6,99,22,45,67]

key = 22
start = 0
end = len(numbers)

for i in numbers:
    if i == key:
        print ("found")
        break
    else:
        print ("Not Found")

found = False

while start < end:
    mid = (start + end)// 2

    if numbers [mid] == key:
        print ("Found element at pos: ",mid)
        found = True
        break
    elif key < numbers[mid]:
        end = mid - 1
    elif key >numbers[mid]:
       start=mid+1
