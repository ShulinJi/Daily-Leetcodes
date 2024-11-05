class Solution:
    def countSubstrings(self, s: str) -> int:
        # def checkPalindrome(subString):
        #     if len(subString) < 2:
        #         return True
        #     i = 0
        #     j = len(subString) - 1
        #     while i < j:
        #         while i < j and not subString[i].isalnum():
        #             i += 1
                
        #         while i < j and not subString[j].isalnum():
        #             j -= 1

        #         if subString[i] != subString[j]:
        #             return False
        #         i += 1
        #         j -= 1

        #     return True


        # counter = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         subString = s[i: j + 1]
        #         if checkPalindrome(subString):
        #             counter += 1

        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count


        counter = 0
        for i in range(len(s)):
            # Odd-length palindromes (single center)
            counter += expand_around_center(i, i)
            # Even-length palindromes (two centers)
            counter += expand_around_center(i, i + 1)
        
        return counter
