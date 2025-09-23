# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

# You are restricted with the following rules:

# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.

 

# Example 1:

# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# Example 2:

# Input: cards = [1,2,1,2]
# Output: false
 

# Constraints:

# cards.length == 4
# 1 <= cards[i] <= 9

class Solution:
    def generate_possible_comb(self, card1, card2):
        # generate all possible results from two cards
        res = [card1 + card2, card1 - card2, card2 - card1, card1 * card2]
        if card1 != 0:
            res.append(card2 / card1)
        if card2 != 0:
            res.append(card1 / card2)
        return res

    # use DFS to try all combinations
    def judgePoint24(self, cards: List[int]) -> bool:
        # base case when only one card left, we evaluate if it is 24 within a tolerance of 0.1 because of floating point precision
        if len(cards) == 1:
            return True if abs(cards[0] - 24) <= 0.1 else False
        
        # try every two cards and replace them with all possible results, then recurse on the new list of cards
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                # create a new list without the two selected cards
                new_list = []
                for x in range(len(cards)):
                    if x != i and x != j:
                        new_list.append(cards[x])
                
                # generate all possible results from the two selected cards
                for res in self.generate_possible_comb(cards[i], cards[j]):
                    new_list.append(res)
                    # recurse
                    if self.judgePoint24(new_list):
                        return True
                    # backtrack
                    new_list.pop()
        
        return False