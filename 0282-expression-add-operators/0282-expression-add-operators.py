class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def dfs(start, prev_val, prev_sum, path):
            if start == len(num) and prev_sum == target:
                ans.append(path)
                return
            # besides above if check, if start>len(num), it will not go inside for loop
            for i in range(start, len(num)):
                if i != start and num[start] == '0':
                    break
                curr_val = int(num[start: i + 1])
                if start == 0: # or, judege by 'path' string is empty or not
                    dfs(i + 1, curr_val, curr_val, path + str(curr_val))
                else:
                    dfs(i + 1, curr_val, prev_sum + curr_val, path + "+" + str(curr_val))
                    dfs(i + 1, -curr_val, prev_sum - curr_val, path + "-" + str(curr_val))
                    dfs(
                        i + 1,
                        prev_val * curr_val, # i.e. diff
                        prev_sum - prev_val + prev_val * curr_val,
                        path + "*" + str(curr_val),
                    )

        dfs(0, 0, 0, "")
        return ans

############

class Solution(object):
  def addOperators(self, num, target):
    res, self.target = [], target
    for i in range(1, len(num) + 1):
      if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
        self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
    return res

  def dfs(self, num, temp, cur, last, res):
    if not num:
      if cur == self.target:
        res.append(temp)
      return
    for i in range(1, len(num) + 1):
      val = num[:i]
      if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
        self.dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
        self.dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
        self.dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val), res)
        '''
            cur - last + last * int(val)

            here the `cur` is the whole/accumlated result from previous recursions
            `cur` is NOT just the previous number
        '''