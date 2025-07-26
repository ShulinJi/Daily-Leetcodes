# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
 

# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].




# Use BFS instead of DFS b/c we want to find minmum path(shortest path), going with DFS will need to explore more paths that does not lead to optimal

# DFS: when needing to explore all possibilities / any/all/ paths => DFS
# BFS: shortest paths
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            curr, steps = queue.popleft()
            if curr == endGene:
                return steps
            
            for c in "ACGT":
                for i in range(len(curr)):
                    # add a mutation, insert a new character and skip one original character (replace)
                    # Python string slicing is safe and forgiving.
                    # Python slicing will never throw an error if curr[i + 1:], i + 1 is bigger than length, it still returns empty string ""
                    # curr[i + 1:] does not cause index out of bound, when i + 1 is equal to the length of the string, Python just returns an empty string ""
                    new_string = curr[:i] + c + curr[i + 1:]
                    if new_string not in visited and new_string in bank:
                        queue.append((new_string, steps + 1))
                        visited.add(new_string)
            
        return -1

            