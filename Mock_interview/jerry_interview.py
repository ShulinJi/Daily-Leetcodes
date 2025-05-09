# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

class Solutions:
    def addup(target, list: input):
        result_list = []
        return_list = []
        queue = []
        queue.append(input[0], 0)
        operation_list = ["+", "-", "nothing"]
        
        def dfs(result_list):
            current_num = queue.pop()
            if current_num[0] == 100 and current_num[1] == (len(input) - 1):
                return_list.extend(result_list)
                return
            elif current_num[0] != 100 and current_num[1] == (len(input) - 1):
                return
                
            for op in operation_list:
                if op == '+':
                    queue.append(current_num[0] + input[current_num[1]] + 1, current_num[1] + 1)
                elif op == '-':
                    queue.append(current_num[0] - (1 + input[current_num[1]]), current_num[1] + 1)
                else:
                    next_num = current_num * 10 + (current_num + 1)
                    queue.append(next_num, current_num[1] + 1)
                
                result_list.append(op)
                dfs(result_list)
                return_list.pop()
                        
            
        dfs(result_list)
        return return_list
            
new_solution = Solutions()
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(new_solution.addup(100, input_array))


# https://leetcode.com/problems/expression-add-operators/



# // There is an array generated by a rule.
# // The first item is 1. If k is in the array, then k*2+1 and k*3+1 are in the array.
# // The array is sorted. There are no duplicate values.
# // Please write a function that accepts an input N. It should return the value of index N of the array.
# // For example [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...] N=10, return 22




# There is an optimal O(n) solution!
import heapq

def array_generator(N):
    min_heap = []
    # base case
    heapq.heappush(min_heap, 1)
    current_operation_num = 0
    current_num = 1
    
    while current_operation_num <= N:
        current_num = heapq.heappop(min_heap)
        while len(min_heap) and current_num == min_heap[0]:
            heapq.heappop(min_heap)
        next_num_smaller = current_num * 2 + 1
        next_num_bigger = current_num * 3 + 1
        heapq.heappush(min_heap, next_num_smaller)
        heapq.heappush(min_heap, next_num_bigger)
        current_operation_num += 1
    
    return current_num
    
N = 100
print(array_generator(N))
        