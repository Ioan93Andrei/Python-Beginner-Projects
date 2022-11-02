# This is going to be a short app to make acronyms out of random words.

phrase = input('Please enter 3 words separated by spaces. ')
words_list = phrase.split()
acronym = []
         
# Adds the first characters of the words to the acronym list.
def append_first_char(letter):
    for letter in words_list:
        if len(letter) >= 3:
            acronym.append(letter[0])

append_first_char(words_list)
final_acronym = ''.join(acronym).upper()
print(f'You have entered the phrase: {phrase}. Your acronym is {final_acronym}.')
