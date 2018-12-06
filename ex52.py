# Define function names()
def names():
    name = str(input('Enter your name: '))
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')
    for letter in name:
        print(letter)
names()
