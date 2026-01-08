# You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

# A pattern is a list of three websites (not necessarily distinct).

# For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

# For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
# Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
# Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
# Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

# Note that the websites in a pattern do not need to be visited contiguously, they only need to be visited in the order they appeared in the pattern.

 

# Example 1:

# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
# Example 2:

# Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
# Output: ["a","b","a"]
 

# Constraints:

# 3 <= username.length <= 50
# 1 <= username[i].length <= 10
# timestamp.length == username.length
# 1 <= timestamp[i] <= 109
# website.length == username.length
# 1 <= website[i].length <= 10
# username[i] and website[i] consist of lowercase English letters.
# It is guaranteed that there is at least one user who visited at least three websites.
# All the tuples [username[i], timestamp[i], website[i]] are unique.

# SECOND ATTEMPT
# The combinations to find all possible 3-sequence takes O(N^3)
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_web = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            user_web[user].append(site)
# for each user, we add the sites in the order of appearance
#         users = {
#   "joe":   ["home", "about", "career"],
#   "james": ["home", "cart", "maps", "home"],
#   "mary":  ["home", "about", "career"]
# }

        # pattern is a dict with key for each pattern and vaue for the score
        pattern = Counter()

        # then we update the pattern for each 
        for user, site in user_web.items():
            # update simply add up
            # we use set because he score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
            # then home, about, about, career, this case home, about, career only score 1 becuase score only
            # based on the number of people, not appearance
            # patterns.update(Counter({("home","about","career"): 1}))
            pattern.update(Counter(set(combinations(site, 3))))
        # return the pattern with max score
        return max(sorted(pattern), key=pattern.get)


# time complexity: O(N^3) where N is the number of website visits (), sorting takes O(N log N)
# space complexity: O(U + P) where U is the number of users and P is the number of patterns
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)

        # The timestamps may not always be pre-ordered (one of the testcases)
		# Sort first based on user, then time (grouping by user)
		# This also helps to maintain order of websites visited in the later part of the solution
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)
        
        patterns = Counter()

        # Get unique 3-sequence (note that website order will automatically be maintained)
		# Note that we take the set of each 3-sequence for each user as they may have repeats
		# For each 3-sequence, count number of users

        # 1. first get all possible 3-sequences combinations(sites, 3)
		# 2. then, count each one once (set)
		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter)) 
		# - updating a dictionary will update the value for existing keys accordingly (int in this case)
        for users, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        # get most frequent 3-sequence sorted lexicographically
        return max(sorted(patterns), key=patterns.get)
