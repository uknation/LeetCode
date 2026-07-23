# python3
class Solution:
    '''
        -   `i` 表示当前处理到字符串 $s$ 的第 $i$ 个字符；
        -   `l` 和 `r` 分别表示剩余待删除的左、右括号的数量；
        -   `t` 表示当前得到的字符串；
        -   `lcnt` 和 `rcnt` 分别表示当前得到的字符串中左、右括号的数量。
    '''
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(i, l, r, lcnt, rcnt, t):
            if i == n:
                if l == 0 and r == 0:
                    ans.add(t)
                return
            if n - i < l + r or lcnt < rcnt:
                return
            if s[i] == '(' and l:
                dfs(i + 1, l - 1, r, lcnt, rcnt, t)
            # note here is elif, not another if, because, to get min-deletion valid string, always delete from extra '(' first
            elif s[i] == ')' and r: 
                dfs(i + 1, l, r - 1, lcnt, rcnt, t)
            # s[i] is a char, or not delete any '(' or ')' so wait for future recursions to do it
            dfs(i + 1, l, r, lcnt + (s[i] == '('), rcnt + (s[i] == ')'), t + s[i])

        l = r = 0
        for c in s: # count how many ( or ) to be removed to get valid one
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = set()
        n = len(s)
        dfs(0, l, r, 0, 0, '') # minimum removal, is archieved by strictly applying counted l/r
        return list(ans)

# bfs version
class Solution(object):
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        '''
        >>> a = {1,2,3,1,2,3}
        >>> a
        {1, 2, 3}
        >>> list(a)
        [1, 2, 3]
        '''
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

# bfs version, python3
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            converted = list(valid)
            if converted: # in python3, valid from filter() will always be not-None, so need to convert to list
                return converted
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

# official-solution: Backtracking. https://leetcode.com/problems/remove-invalid-parentheses/editorial/
class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        # If we have reached the end of string.
        if index == len(string):

            # If the current expression is valid. The only scenario where it can be
            # invalid here is if left > right. The other way around we handled early on in the recursion.
            if left_count == right_count:

                if rem_count <= self.min_removed:
                    # This is the resulting expression.
                    # Strings are immutable in Python so we move around a list in the recursion
                    # and eventually join to get the final string.
                    possible_ans = "".join(expr)

                    # If the current count of brackets removed < current minimum, ignore
                    # previous answers and update the current minimum count.
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)    
        else:        

            current_char = string[index]

            # If the current character is not a parenthesis, just recurse one step ahead.
            if current_char != '(' and  current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                # Else, one recursion is with ignoring the current character.
                # So, we increment the ignored counter and leave the left and right untouched.
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)

                expr.append(current_char)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)

                expr.pop()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


# official-solution: Limited Backtracking. https://leetcode.com/problems/remove-invalid-parentheses/editorial/
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])     
        return list(result.keys())

############

class Solution(object):
  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """

    def isValid(s):
      stack = []
      for c in s:
        if c == "(":
          stack.append("(")
        elif c == ")":
          stack.append(")")
          if len(stack) >= 2 and stack[-2] + stack[-1] == "()":
            stack.pop()
            stack.pop()
      return len(stack)

    def dfs(s, res, cache, length):
      if s in cache:
        return

      if len(s) == length:
        if isValid(s) == 0:
          res.append(s)
          return

      for i in range(0, len(s)):
        if s[i] == "(" or s[i] == ")" and len(s) - 1 >= length:
          dfs(s[:i] + s[i + 1:], res, cache, length)
          cache.add(s[:i] + s[i + 1:])

    prepLeft = ""
    for i in range(0, len(s)):
      if s[i] == "(":
        prepLeft += s[i:]
        break
      elif s[i] != ")":
        prepLeft += s[i]

    prepRight = ""
    for i in reversed(range(0, len(prepLeft))):
      if prepLeft[i] == ")":
        prepRight += prepLeft[:i + 1][::-1]
        break
      elif prepLeft[i] != "(":
        prepRight += prepLeft[i]

    s = prepRight[::-1]
    length = len(s) - isValid(s)
    res = []
    cache = set()
    dfs(s, res, cache, length)
    return res