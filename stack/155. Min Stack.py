class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            # first one is current num
            # second one is current minimum
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            # keep track of current minimum
            self.stack.append((val, min(val, current_min)))
        return 
        
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]










    def __init__(self):
        self._stack = []
        self._min_stack = []
        
    def push(self, val: int) -> None:
        # whenever we push a value to the stack, we check if it a new minimum and track the minimum of the stack all the time by appending the minimum of current stack to the min_stack
        if not self._min_stack or val < self._min_stack[-1]:
            self._min_stack.append(val)
        else:
            self._min_stack.append(self._min_stack[-1])
        self._stack.append(val)

    def pop(self) -> None:
        # whenever we pop a value, we pop the min_stack as well to reflect the current minimum
        self._stack.pop()
        self._min_stack.pop()
    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        # current minimum is the last element of the min_stack
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
