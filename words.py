# -*- coding: utf-8 -*-

import sys

def makeTitle(sentence):
    return sentence.title()
def makeUpper(sentence):
    return sentence.upper()
def makeLower(sentence):
    return sentence.lower()
def countWords(sentence):
    words = [word for word in sentence.split(' ')]
    return len(words)
def countLetter(sentence, letter):
    return sentence.count(sentence)
def makeNewWord(sentence):
    words = [w for w in sentence.split(' ')]
    newWord = '%s%s' % (words[0],words[-1])
    return newWord
def makeAcronym(sentence):
    acronym = ''
    for word in sentence.upper().split():
        acronym += word[0]
    return acronym


def main():
    sentence = input('Please enter a sentence: \n')
    letter = input('Enter a letter : ')
    print(makeTitle(sentence))
    print(makeUpper(sentence))
    print(makeLower(sentence))
    print('There are %s words in your sentence' % (countWords(sentence)))
    print('Your sentence contains %s \"%s\"' % (
        countLetter(sentence, letter), letter))
    print('%s is a new word made from your input' % (makeNewWord(sentence)))
    print('The acronym for your sentence is %s' % (makeAcronym(sentence)))

if __name__ == '__main__':
    main()