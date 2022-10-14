"""
word occurrences
estimated:35
actual:
"""

number_of_letters = {}
sentence = input("sentence: ").split(" ")

for word in sentence:
    if word not in number_of_letters:
        number_of_letters.update({word:int(1)})
    else:
        number_of_letters[word] = number_of_letters.get(word) + 1

sorted_number_of_letters = (sorted(number_of_letters.items()))
for words in sorted_number_of_letters:
    print(words)