# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

# Example 1:

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:

# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:

# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.
 

# Constraints:

# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.


# O(4(d + 10^4)) time | O(4(d + 10^4)) space with BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # d is the number of deadends, 10^4 is the number of all possible combinations of the lock
        # next_slot and prev_slot are used to generate new combinations of the lock. Next slot is the next number in the wheel, and prev slot is the previous number in the wheel.
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        # visited_combination used to store all the combinations that have been visited, so we don't visit them again
        visited_combination = set(deadends)
        pending_combination = deque()

        if "0000" in visited_combination:
            return -1 

        turn = 0
        pending_combination.append("0000")
        while pending_combination:
            # current_level_count is the number of combinations in the current level of the BFS tree
            current_level_count = len(pending_combination)
            for _ in range(current_level_count):
                current_combination = pending_combination.popleft()
                if current_combination == target:
                    return turn
                # generate new comb with next_slot and prev_slot, each with 4 wheels, so we have 4 * 2 = 8 new combinations
                for i in range(4):
                    new_list = list(current_combination)
                    # new combination with next slot
                    new_list[i] = next_slot[new_list[i]]
                    new_combination = "".join(new_list)
                    if new_combination not in visited_combination:
                        pending_combination.append(new_combination)
                        # add the new combination to the visited_combination set in the same time to avoid duplicates
                        visited_combination.add(new_combination)
                    
                    new_list = list(current_combination)
                    # new combination with previous slot
                    new_list[i] = prev_slot[new_list[i]]
                    new_combination = "".join(new_list)
                    if new_combination not in visited_combination:
                        pending_combination.append(new_combination)
                        visited_combination.add(new_combination)

            turn += 1

        return -1
        


