class Solution:
    def reverse(self, x: int) -> int:
        stringInput = str(x)
        if stringInput[0] == '-':
            tmp = int(stringInput[-1:0:-1])
            return -tmp
        elif stringInput[0] == '0':
            tmp = int(stringInput[-1:0:-1])
            return tmp
        else:
            tmp = int(stringInput[::-1])
            return tmp
        
if __name__ == '__main__':
    sol = Solution()
    answer = sol.reverse(-123)
    print(answer)