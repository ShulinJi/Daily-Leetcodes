# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

# SECOND ATTEMPT
class Solution:
    def myAtoi(self, s: str) -> int:
        # sign default is positive
        sign = 1
        result = 0 # the digital number
        # used to check overflow and underflow
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        index = 0

        # skip all the white space at the front
        while index < len(s) and s[index].isspace():
            index += 1
        
        # check the sign at the front
        if index < len(s) and s[index] == "+":
            sign = 1
            index += 1
        elif index < len(s) and s[index] == "-":
            sign = -1
            index += 1
        
        # if we meet any non-digital, stop iter 
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            # to check overflow/underflow, 
            # if result is bigger than INT_MAX // 10 = 214748364, any bigger than this, say 214748365, if we append a 
            # another digit behind that, it will overflow! and if say 214748363, samller than, then we can append any digit without worrying overflow, and if equals, then we need to compare the next digit if it is smaller than 7
            # 
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                # we have aoverflow
                return INT_MAX if sign == 1 else INT_MIN
            
            # continue to form number
            result = result * 10 + digit
            index += 1
        
        return sign * result


class Solution:
    def myAtoi(self, input: str) -> int:
        # Official solution with overflow check!
        sign = 1
        result = 0
        index = 0
        n = len(input)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == " ":
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and input[index] == "+":
            sign = 1
            index += 1
        elif index < n and input[index] == "-":
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])

            # Check overflow and underflow conditions.
            if (result > INT_MAX // 10) or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result

