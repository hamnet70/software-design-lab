# This program takes a functional approach to the word search and indexing.


# I honestly don't see how on earth this first function is either callable or useable (with no defined unsavory characters variable or list)
def remove_characters (string, unsavory_characters):
    outstring = ""
    
    for characters in string:
        if characters not in unsavory_characters:
            outstring += characters
    return outstring



def clean_string(string):
    string_without_punct = remove_characters(string, [".", ","])
    string_lower_case = string_without_punct.lower()

    return string_lower_case

def tokenize(string, preprocess=False):
    if preprocess:
        string = clean_string(string)

    word_list = string.split()

    return word_list


def count_occurances(word_list, word_to_match):
   
    word_match_counter = 0

    for word in word_list:
        if word == word_to_match:
            word_match_counter += 1

    return word_match_counter 


def words_matching_first_character(word_list, match_character):

    words_beginning_with_character = []

    for word in word_list:
        if word[0] == match_character:
            words_beginning_with_character.append(word)

    return words_beginning_with_character


if __name__ == '__main__':
    original_text = "Nature's first green is gold, her hardest hue to hold, her early leaf's a flower, but only so an hour."
    tokens = tokenize(original_text, True)

    print("Total words:", len(tokens))

    print('Number of occurances of word match:', count_occurances(tokens, 'her'))

    print("Words beginning with character:", words_matching_first_character(tokens, 'h'))

    print("Number of words beginning with character:", len(words_matching_first_character(tokens, 'h')))
