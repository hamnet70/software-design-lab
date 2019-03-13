# This program detects the burningness of a user's question and answers accordingly.

# random.randint(x, y)

import random

def is_burning(question):
    
    burning_words = [
        'ever',
        'really',
        'need',
        'ache',
        'never'
    ]
    
    burning = False

    for word in burning_words:
        if word in question:
            burning = True

    return burning

    
   


# print(is_burning(input("Ask me a question.  ")))
## 1) For Lauren: we started wtih this line and a duplicate with a burning word: print(is_burning("Will it snow tomorrow?"))


def answer_question(question):

    burning_answers = [
        'Absolutely',
        'HELL, no',
    ]

    cold_answers = [
        'Sure...',
        'Maybe',
        "Meh",
        "Sigh",
    ]

    if is_burning(question):
        answer = random.choice(burning_answers)
    else:
        answer = random.choice(cold_answers)

        formatted_answer = format_answer(answer)

    #return answer
    return formatted_answer



def format_answer(answer):
    """Take an answer as a string and add HTML formatting to it"""

    html_begin = "<html><body><p>"
    html_end = "</p></body></html>"

    formatted_answer = html_begin + answer + html_end

    return formatted_answer

#print(answer_question(input("Ask a question.  ")))
print(answer_question("Is it raining?"))




