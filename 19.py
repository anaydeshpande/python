# coding=utf-8

pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beauty'
pirate['professor']='foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your']='yer'
pirate['excuse']='arr'
pirate['students']='swabbies'
pirate['are']='be'
pirate['lawyer']='foul blaggart'
pirate['the']='th’'
pirate['restroom']='head'
pirate['my']='me'
pirate['hello']='avast'
pirate['is']='be'
pirate['man']='matey'


sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
