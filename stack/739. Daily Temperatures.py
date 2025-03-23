# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:





        # O(n) and O(n)
        stack = [] # store the previous temperature data
        answer = [0] * len(temperatures)

        for curr_day, curr_temp in enumerate(temperatures):
            # if current temp is higher than previous temp, we pop the stack and calculate the day diff.
            while stack and stack[-1][0] < curr_temp:
                prev_data = stack.pop()
                prev_day = prev_data[1]
                answer[prev_day] = curr_day - prev_day
            stack.append((curr_temp, curr_day))
        
        return answer



# Optimized solution, O(n) and O(1), but not as intuitive as previous
        class Solution:
            def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                n = len(temperatures)
                hottest = 0
                answer = [0] * n
                
                for curr_day in range(n - 1, -1, -1):
                    current_temp = temperatures[curr_day]
                    if current_temp >= hottest:
                        hottest = current_temp
                        continue
                    
                    days = 1
                    while temperatures[curr_day + days] <= current_temp:
                        # Use information from answer to search for the next warmer day
                        days += answer[curr_day + days]
                    answer[curr_day] = days

                return answer