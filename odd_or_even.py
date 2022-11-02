def odd_or_even():

    number = int(input('Please enter the number: '))

    if number % 2  == 0:
        print(f'{number} is an odd number.')
    else:
        print(f'{number} is not an even number.')

odd_or_even()

# There is an error when the division results in a float number