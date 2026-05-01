text ="I am Nancy and I am a developer in Fiserv. Today, I resigned because of dissatisfaction with my work profile."

text_word = text.split()

word_count = {word: text_word.count(word) for word in text_word}
key = [key for key, value in word_count.items() if value==max(word_count.values())]

# print(text_word)
# for word in text_word:
#     cnt = text_word.count(word)
#     word_count[word] = cnt
#
# print(word_count)
# max_occur = max(word_count.values())

print("max appearance word is", key)


