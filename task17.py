from statistics import mean, median

arr = [1, 2, 3, 4, 1, 5, 15, 6]
m, M = min(arr), max(arr)
i, j = arr.index(m), arr.index(M)
if i < j:
    print(mean(arr[i:j]))
else:
    arr[i] = arr[j] = median(arr[j:i])

print(arr)
