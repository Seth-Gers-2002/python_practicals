"""
word occurrences
estimated:35
actual: 1hr, 10 mins
"""

number_of_letters = {}
sentence = input("sentence: ").split(" ")

for word in sentence:
    if word not in number_of_letters:
        number_of_letters.update({word:int(1)})
    else:
        number_of_letters[word] = number_of_letters.get(word) + 1

sorted_number_of_letters = (sorted(number_of_letters.items()))

max_length = max(len(name) for name in number_of_letters)

for word in sorted_number_of_letters:
    print(f"{word[0]:{max_length}} {word[1]}")