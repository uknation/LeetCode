class Solution:
    def calculate(self, s: str) -> int:
        v, n = 0, len(s)
        sign = '+'
        stk = []
        for i, c in enumerate(s):
            if c.isdigit():
                v = v * 10 + int(c)
            if i == n - 1 or c in '+-*/':
                if sign == '+':
                    stk.append(v)
                # for "10-2*5": when '-' encountered, var 'sign' is still '+'
                # so '10' will be pushed to stk before setting sign to '-'
                elif sign == '-':
                    stk.append(-v)
                elif sign == '*':
                    stk.append(stk.pop() * v)
                elif sign == '/':
                    stk.append(int(stk.pop() / v))
                else:
                    print("operator not supported")

                sign = c # reset inside 'if'
                v = 0
        return sum(stk)