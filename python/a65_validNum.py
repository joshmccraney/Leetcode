class Solution:
    def isNumber(self, s):
        if s[0] in ('+', '-'):
            s = s[1:]
            
        if (s[0] == 'E') or (s[0] == 'e') or (s == '.') or (s[-1] == 'E') or (s[-1] == 'e'): return False

        set = {'E', 'e', '.'}

        for i in range(len(s)):
            if  s[i].isdigit():
                continue

            elif s[i] == 'E' or s[i] == 'e':
                set.clear()

            elif s[i] == '.':
                set.remove('.')
                
                for j in range(i+1, len(s)):
                    if s[j].isdigit: continue
                    elif s[j] not in set: return False

            else: return False
        return True

if __name__ == "__main__":
    ob1 = Solution()
    s = ".."
    print(ob1.isNumber(s))