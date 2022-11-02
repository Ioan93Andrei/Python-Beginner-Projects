def odd_or_even():

    number = int(input('Please enter the number: '))

    if number % 2  == 0:
        print(f'{number} is an ODD number.')
    else:
        print(f'{number} is an EVEN number.')

odd_or_even()

# There is an error when the division results in a float number