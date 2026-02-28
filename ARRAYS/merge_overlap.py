intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
intervals.sort()
merged = []
for i in intervals:
    if not merged or merged[-1][1] < i[0]:
        merged.append(i)
    else:
        merged[-1][1] = max(merged[-1][1], i[1])
print(merged)