def majority_element(arr):
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate if arr.count(candidate) > len(arr) // 2 else None
arr = [1, 2, 3, 1, 1, 1, 2, 1, 1]
print("Majority element:", majority_element(arr))
