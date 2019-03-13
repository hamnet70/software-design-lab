# This program reverses the word order of a user-generated sentence



def sentence_flip(sentence):
    ordered = sentence.split(" ")
    reordered = []

    number = len(ordered)

    while number != 0:
        reordered.append(ordered[number-1])
        number -= 1
    
    #return reordered
    return " ".join(reordered)

   





print(sentence_flip(input("Type in a sentence or series of words without punctuation:   ")))


 






