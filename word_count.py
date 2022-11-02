def count_words():
    phrase = input('Please enter the phrase you want to be counted: ')
    words_list = phrase.split()
    print(f'Your phrase has {len(words_list)} words.')

count_words()