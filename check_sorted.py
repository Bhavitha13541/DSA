class Solution:
    def check_sorted_roated(self, num):
        n = len(num)
        count = 0
        for i in range(n):
            if num[i] > num[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        return True