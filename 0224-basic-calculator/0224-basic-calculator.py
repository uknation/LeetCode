# only + and - , no * , no / 
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        ans, sign = 0, 1
        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                x = 0
                j = i
                # with this while, no need to do final calculation like below solution
                while j < n and s[j].isdigit():
                    x = x * 10 + int(s[j])
                    j += 1
                ans += sign * x
                i = j - 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans = stk.pop() * ans + stk.pop()
            i += 1
        return ans

#############

class Solution:
  def calculate(self, s: str) -> int:
    ans = 0
    num = 0
    sign = 1
    stack = [sign]  # stack[-1]: current env's sign

    for c in s:
      if c.isdigit():
        num = num * 10 + int(c)
        # num = num * 10 + (ord(c) - ord('0')) => also works
      elif c == '(':
        stack.append(sign)
      elif c == ')':
        stack.pop() # pop pairing sign for this () pair
      elif c == '+' or c == '-':
        ans += sign * num
        sign = (1 if c == '+' else -1) * stack[-1] # after all + or -, the sign for current num
        num = 0

    return ans + sign * num # final calculation