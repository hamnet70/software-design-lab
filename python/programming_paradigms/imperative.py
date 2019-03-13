# This program is from the Programming Paradigms reading
# I thought it would be good practice to recreate it myself

text = "Let me not to the marriage of true minds admit impediments. Love is not love which alters when it alteration finds nor bends with the remover to remove."

unwanted_characters = [",", "."]
string_without_punct = ""

for characters in text:
    if characters not in unwanted_characters:
        string_without_punct += characters

lower_case_string = string_without_punct.lower()

word_list = lower_case_string.split()

word_list_length = len(word_list)


print("That string is %d words long." % word_list_length)

word_to_search = "love"
word_search_counter = 0

for word in word_list:
    if word == word_to_search:
        word_search_counter += 1

print("That word appears %d times." % word_search_counter)


match_character = "a"
letter_counter = 0
words_beginning_with_letter = []

for word in word_list:
    if word[0] == match_character:
        letter_counter += 1 
        words_beginning_with_letter.append(word)

print("There are %d words starting with that letter: " %letter_counter)
print(words_beginning_with_letter)