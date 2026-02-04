# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# O(1) for runtime of put and get and O(capacity) for space
# create a class for list nodes
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # a single hashmap is not enough because of capacity, when capacity exceeds we cannot just randomly
    # evict a kv pair, we need to evict the least recently used ones!
    # we put the key at the back when we used it, and remove the front one

    # Use doubly linked list(have prev and next both way) so that we can delete a node at any postion
    # Need reference for both tail and head b/c we need tail so that we can add new value and update
    # Need reference for head b/c need to remove the LRU node
    def __init__(self, capacity: int):
        self.capacity = capacity

        # use dictionary to allow O(1) finding time to find a node
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        # initialize the doubly linked list 
        self.head.next = self.tail
        self.tail.prev = self.head

    # we need to move the node to the back, and the current node can be at anywhere, so we need the functionality of deletion from anywhere. O(1) of finding the node by hashmap, O(1) deletion in doubly linked list, ex. delete C simply B.next = D since we have prev (C.prev = B) and next (D)
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        # remove the node and add it to the end
        self.remove(node)
        self.add(node)
        return node.val

    # need to update or insert in hashmap
    # if existing in the hashmap, remove the old node, and add the new node to the back 
    def put(self, key: int, value: int) -> None:
        # if existing in the hashmap, delete the node (because we accessed it)
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        
        # add new node to the back
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        # if inserting a node exceeds the limit, then we delete the front
        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]
    
    # add a node to the end of the doubly linked list
    def add(self, node):
        previous_end = self.tail.prev
        # update 4 links between 3 nodes (2 prev, 2 next)(last tail, current new tail, fake tail)
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# a doubly linked list
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# SECOND ATTEMPT with debug messages
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_back(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        self.tail.prev = node
        node.next = self.tail

    def print_list(self):
        value_list = []
        temp_head = self.head
        while temp_head.next:
            value_list.append(temp_head.value)
            temp_head = temp_head.next
        print(value_list)
    # to get a key, if key not in the 
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        curr_node = self.dict[key]
        self.remove(curr_node)
        self.add_to_back(curr_node)
        # self.print_list()

        return curr_node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            curr_node = self.dict[key]
            self.remove(curr_node)

        new_node = ListNode(key, value)
        self.add_to_back(new_node)
        self.dict[key] = new_node
        if len(self.dict) > self.capacity:
            del self.dict[self.head.next.key]
            self.remove(self.head.next)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




# Using built-in data structure:

# In Java, we will be using LinkedHashMap, which is a hash map that maintains insertion order. It essentially implements the linked list for us in the same data structure as the hash map, with the add and remove methods built into the hash map operations.

# In C++, we will be using std::list, which implements the doubly linked list.

# In Python, we will be using collections.OrderedDict. This is similar to the Java data structure - it is a hash map that maintains insertion order.


import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)