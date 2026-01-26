# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.
 

# Constraints:

# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104

# SECOND ATTEMPT, better explanation
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0
        currentGas = 0
        startPoint = 0

        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            totalGas += gas[i]
            totalCost += cost[i]

            # if our current gas is below 0, let's say starting from 0 then first time we have negative, 
            # it means all previous stations are notpossible start point because we never below 0 until now, 
            # which means previous station are all helping us (net gas >= 0) for all indices before current index, and starting from any of the 
            # stations between 0 to current station will reduce even more because we reduce the help by choosing
            # 0 < k < current station! because any station in between those stations would be net >= 0
            # then, we choose to start from the next station!
            if currentGas < 0:
                startPoint = i + 1
                currentGas = 0
            
        if totalCost > totalGas:
            return -1
        
        return startPoint

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Brutal Force
        # for x in range(len(gas)):
        #     currentStation = x

        #     # if the starting point does not have any gas, skip it
        #     if gas[currentStation] == 0:
        #         continue

        #     totalGas = 0
        #     i = 0 # used to track circular track
        #     while totalGas >= 0:
        #         if i == len(gas):
        #             return x
        #         totalGas += gas[currentStation]
        #         totalGas -= cost[currentStation]
                
        #         # circular shape
        #         if currentStation + 1 != len(gas):
        #             currentStation += 1
        #         else:
        #             currentStation = 0
        #         i += 1

        # return -1

# Greedy Algorithms
# as we can't make the trip starting at very beginning we can't make over here at index 1 or index 2 or index 3
#  don't need to check previous points if current one fails since 
# don't need to worry about if our gas is enough to cover the deficit before because if we have a solution
# Then total gas MUST be greater than or equal to toal cost => if we have a solution, else no solution
# Only need to know if currentGas is smaller than 0!

        current_gas = 0
        total_gas = 0
        total_cost = 0
        start_point = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_point = i + 1
                current_gas = 0
        
        if total_cost > total_gas:
            return -1
        
        return start_point
