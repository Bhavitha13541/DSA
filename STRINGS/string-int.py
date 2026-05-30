class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0

        # skip spaces
        while i < len(s) and s[i] == ' ':
            i += 1

        sign = 1

        # check sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        num = 0

        # read digits
        while i < len(s) and s[i].isdigit():
          num = num * 10 + int(s[i])
          i += 1

        # apply sign
        num = num * sign

        # clamp range
        INT_MIN = -(2**31)
        INT_MAX = (2**31 - 1)

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
sol = Solution()
print(sol.myAtoi('  -42'))
# -42
print(sol.myAtoi("1337c0d3"))
# 1337
print(sol.myAtoi("0-1"))
# 0