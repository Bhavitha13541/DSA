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