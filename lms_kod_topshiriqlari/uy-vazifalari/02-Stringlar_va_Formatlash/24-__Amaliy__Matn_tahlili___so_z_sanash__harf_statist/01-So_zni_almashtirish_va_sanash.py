text = input()
word = input()

word_count = text.count(word)

new_text = text.replace(word, word.upper())

print(new_text)
print(word_count)