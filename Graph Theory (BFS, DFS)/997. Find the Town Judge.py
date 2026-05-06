# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 

# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n


# could be better because there could not be two judges at the same time because two judges would trust each other!
# so we don't nbeed the judge_exist variable, we can just return -1 if we find two judges
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trusted_numbers = [0] * (n + 1)
        trust_numbers = [0] * (n + 1)
        # we record the number of times that each person being trusted
        for relationship in trust:
            trusted_numbers[relationship[1]] += 1
            trust_numbers[relationship[0]] += 1        
  
        judge_exist = False
        current_judge = -1
        for i in range(len(trusted_numbers)):
            if trusted_numbers[i] == n - 1 and trust_numbers[i] == 0:
                if judge_exist:
                    return -1
                else:
                    judge_exist = True
                    current_judge = i
        
        return current_judge


# O(E) and O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if there are less than n - 1 entries, it means there couldn't be one to be trusted by everyone
        if len(trust) < n - 1:
            return -1

        trusted = [0] * (n + 1)
        be_trusted = [0] * (n + 1)

        # for each entry, we increment the trust and be_trusted 
        for a, b in trust:
            trusted[a] += 1
            be_trusted[b] += 1
        
        # There couldn't be more than 1 judges b/c if there are two judges, they would have to trust each other, but a judge cannot trust anyone, so it is against the rule

        # and if we find any entries that satisfy all the conditions
        for i in range(1, n + 1):
            if be_trusted[i] == n - 1 and trusted[i] == 0:
                return i
        
        return -1
