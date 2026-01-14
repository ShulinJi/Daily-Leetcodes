# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
 

# Constraints:

# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

# SECOND ATTEMPT
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # first we have a subfunction to form a line
        def find_word(i):
            current_length = 0
            current_line = []
            # current_length + len(words[i]) <= maxWidth, no +1 bc last words can without whitepace
            while i < len(words) and current_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                # we use +1 bc the each word needs to followed by a whitespace
                current_length += len(words[i]) + 1
                i += 1
            
            return current_line
        
        # another function to padding the whiteaspace to current line
        def form_line(i, line):
            # we start with -1 because the last word can leave without white space
            base_length = -1
            for word in line:
                # defalt length with one extra space
                base_length += len(word) + 1
            
            # how may extra spaces we have that needs to take care (whitespaces to add)
            extra_space = maxWidth - base_length
            # if we are dealing with last line, it is left-justified
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_space

            # -1 because we are ignoring the last word, don't need white space
            words_need_padding = len(line) - 1
            # those many whitespaces that needs to pad for each word except last one
            padding_space = extra_space // words_need_padding
            # cannot distribute evenly, need to padd extra ones starting from left
            extra_uneven_padding = extra_space % words_need_padding

            # pad those uneven ones first
            for i in range(extra_uneven_padding):
                line[i] += " "
            
            # now we pad the evenly distributed ones
            for i in range(words_need_padding):
                line[i] += " " * padding_space
            
            # now we add the default one after each word by join with " "
            return " ".join(line)
        
        ans = []
        i = 0
        while i < len(words):
            newline = find_word(i)
            i += len(newline)
            ans.append(form_line(i, newline))

        return ans


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words(i):
            current_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return current_line

        def create_line(line, i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1

            extra_spaces = maxWidth - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces

            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "

            for j in range(word_count):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        ans = []
        i = 0

        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            ans.append(create_line(current_line, i))

        return ans
