class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ch_list = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits)==0:
            return []

        after = self.letterCombinations(digits[1:])
        if len(after)==0:
            return [x for x in ch_list[int(digits[0])]]

        return [ m+n for m in ch_list[int(digits[0])] for n in after ]

print(Solution().letterCombinations("234"))
print([m+n] for m in "abc" for n in [])

