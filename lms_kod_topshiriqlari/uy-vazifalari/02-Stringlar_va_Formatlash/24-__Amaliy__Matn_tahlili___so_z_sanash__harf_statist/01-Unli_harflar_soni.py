text = input().lower()

vowels_count = (text.count('a') + 
                text.count('e') + 
                text.count('i') + 
                text.count('o') + 
                text.count('u'))

print(vowels_count)