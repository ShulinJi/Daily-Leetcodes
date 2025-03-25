

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# Given 3 lists of words, returns the words that occur in all 3 lists. You can assume all 3 input lists are the same size and each input list does not contain any duplicates.

# Example 1:
# Input - ["hi", "bye"], [ "why", "lie" ], ["try", "cry"]
# Output - []

# Example 2:
# Input - [ "hi", "bye" ], [ "bye", "lie" ], ["try", "cry"]
# Output - []

# Example 3:
# Input - [ "hi", "bye"], [ "bye", "lie"], ["bye", "cry"]
# Output - [ "bye" ]





Input = [[ "hi", "bye"], ["lie", "bye"], ["bye", "hi"]]
word_dict = {}
word_set = set()
n = len(Input) # length of total lists
res = []

# first go through all the lists to populate the dictionary to find all the frequency of each word
for x in range(n):
    for word in Input[x]:
        if word in word_set:
            continue
        else:
            word_set.add(word)
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    word_set.clear()

for i, value in enumerate(word_dict.items()):
    if value[1] >= 2:
        res.append(value[0])

print(res)



# 1. Explain your idea to interviewer before you code
# 2. More practises and more familiar with data structure and keywords
# 3. Read the error message thoroughfully, inclduing the line number
# 4. When done with your coding, run the tests yourself and test with different cases before actaully saying you are done with the answer
# 5. 