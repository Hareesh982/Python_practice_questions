li = [1,2,3,4,5,6]
value = 1
low = 0
high = len(li)-1
while True:
    mid = (low+high)//2
    if li[mid] == value:
        print(f"{value} foound at index {mid}")
        break
    elif value < li[mid]:
        high = mid - 1
    else:
        low = mid + 1
