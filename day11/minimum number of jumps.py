arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
if n <= 1:
    jumps = 0
else:
    jumps, farthest, current_end = 0, 0, 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break
print("Minimum number of jumps:", jumps)
