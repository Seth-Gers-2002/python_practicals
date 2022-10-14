"""
word occurrences
estimated:35
actual:
"""

stored = {}
sentence = input("sentence: ").split(" ")

for word in sentence:
    if word not in stored:
        stored.update({word:int(1)})
    else:
        stored[word] = stored.get(word) + 1
print(stored)