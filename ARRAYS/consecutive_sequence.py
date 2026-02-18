arr = [100, 4,200, 1, 3, 2]
s = set(arr)
sequences = []
for num in s:
    if num - 1 not in s:
        current = num
        seq = [current]
        while current + 1 in s:
            current += 1
            seq.append(current)
        sequences.append(seq)
longest = max(sequences, key = len)
print("the longest consecutive sequence is : ", len(longest))

# output:
# the longest consecutive sequence is :  4

#  USING FUNCTIONS
def longestConsecutive(arr):
    s = set(arr)
    sequences = []
    for num in s:
        if num - 1 not in s:
            current = num
            seq = [current]
            while current + 1 in s:
                current += 1
                seq.append(current)
            sequences.append(seq)
    longest = max(sequences, key = len)
    return len(longest)
arr = [100, 1,400, 4,5,3,2]
print("the longest consecutive sequence is : ", longestConsecutive(arr))

# output:
# the longest consecutive sequence is :  5
