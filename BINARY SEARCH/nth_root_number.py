def NthrootNumber(n, m):
    low = 1
    high = m 
    
    while low <= high:
        mid = (low + high) // 2
        val = mid ** n
        if val == m:
            return mid
        if val < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
NthrootNumber(3, 27)
print(NthrootNumber(3, 27),
      NthrootNumber(4,69))

# output:
# 3
# -1