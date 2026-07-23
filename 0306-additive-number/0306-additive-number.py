class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def dfs(startIndex: int, out: List[int]) -> bool:
            # equal check is here
            if len(out) >= 3 and out[-1] != out[-2] + out[-3]:
                return False
            if startIndex == len(num):
                return len(out) >= 3

            for i in range(startIndex, len(num)):
                current = num[startIndex: i + 1]
                if (len(current) > 1 and current[0] == '0'):
                    break

                out.append(int(current))
                if dfs(i + 1, out):
                    return True
                out.pop()

            return False

        if not num:
            return False
        return dfs(0, [])

#############

# follow up: super large number, solve overflow issue
class Solution:
    def addStrings(num1: str, num2: str) -> str:
        carry = 0
        result = []
        
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            sum = x + y + carry
            result.append(str(sum % 10))
            carry = sum // 10
            i, j = i - 1, j - 1
        
        return ''.join(reversed(result))

    def isAdditiveNumber(num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                while j < n:
                    sum = addStrings(num1, num2)
                    if not num.startswith(sum, j):
                        break
                    j += len(sum)
                    num1, num2 = num2, sum
                    if j == n:
                        return True
        return False

#############

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(a, b, num):
            if not num:
                return True
            if a + b > 0 and num[0] == '0':
                return False
            for i in range(1, len(num) + 1):
                if a + b == int(num[:i]):
                    if dfs(b, a + b, num[i:]):
                        return True
            return False

        n = len(num)
        for i in range(1, n - 1): # 1st cut
            if i > 1 and num[0] == '0': # 0 + 1 = 1 is fine, but 00 + 1 is wrong
                break
            for j in range(i + 1, n): # 2nd cut, so making it a 3-segments
                if j - i > 1 and num[i] == '0':
                    break
                if dfs(int(num[:i]), int(num[i:j]), num[j:]): # better than below, early stop
                    return True
        return False