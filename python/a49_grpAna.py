class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for str in strs:
            x = ''.join(sorted(str))
            if x not in d:
                d[x] = [str]
            else:
                d[x].append(str)
        return d.values()

if __name__ == "__main__":
    ob1 = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(ob1.groupAnagrams(strs))