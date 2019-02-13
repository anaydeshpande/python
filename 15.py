x = input("Enter a sentence")

x = x.lower()   # convert to all lowercase
print x

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = sorted(letter_count.keys())
for char in keys:
    print char, letter_count[char]