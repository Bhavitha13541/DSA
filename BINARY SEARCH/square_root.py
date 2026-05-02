# BRUTE FORCE APPROACH


# N = 28
# for i in range(N+1):
#     if i*i == N:
#         print(i)
#         break
#     elif i *i > N:
#         print(i - 1)
#         break

#   OPTIMIZED APPROACH

def square_root(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return high
print(square_root(28), square_root(34), square_root(36), square_root(25))

# output: 5 5 6 5