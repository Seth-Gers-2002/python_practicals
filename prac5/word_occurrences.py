"""
word occurrences
estimated:40
actual:
"""

stored = []
sentence = input("sentence: ").split(" ")

for word in sentence:
    if word not in stored:
        stored.append(word)
    else:
        print("ahh")

print(stored)