# First Paragraph
# import modules
import os
import re
# defined a function to take the average from a list of numbers 
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
# set the path 
text_file = os.path.join('Downloads', 'paragraph_1 (1).txt')
# opened the text file
with open(text_file, 'r') as p_file:
    paragraph = p_file.read()

# used list comphrension inside the function call. 
wordList = paragraph.split(" ")
# created a list that consists of the number of words in a sentence, then averaged it. 
wordCount = len(wordList)
sentenceList =  re.split("(?:[.!?]) +", paragraph)
sentenceCount = len(sentenceList)
avgWordsPerSentence = mean([len(sentence.split(" ")) for sentence in sentenceList])
avgLettersPerWord = mean([len(word) for word in wordList])
# printed the measures 
print("Word Count: {}".format(wordCount))
print("Sentence Count: {}".format(sentenceCount))
print("Average Words per Sentence: {}".format(avgWordsPerSentence))
print("Average Letters per Word: {}".format(avgLettersPerWord))

# Second Paragraph
# import modules
import os
import re
# defined a function to take the average from a list of numbers 
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
# set the path 
text_file2 = os.path.join('Downloads', 'paragraph_2.txt')
sentence_re = re.compile(r"(?:[.!?])|(?:\n|\n\r:) +", re.MULTILINE)
# opened the text file
with open(text_file2, 'r') as p_file:
    paragraph = p_file.read()
# used list comphrension inside the function call. 
wordList = paragraph.split(" ")
# created a list that consists of the number of words in a sentence, then averaged it. 
wordCount = len(wordList)
sentenceList =  re.split(sentence_re, paragraph)
sentenceCount = len(sentenceList)
avgWordsPerSentence = mean([len(sentence.split(" ")) for sentence in sentenceList])
avgLettersPerWord = mean([len(word) for word in wordList])
# printed the measures 
print("Word Count: {}".format(wordCount))
print("Sentence Count: {}".format(sentenceCount))
print("Average Words per Sentence: {}".format(avgWordsPerSentence))
print("Average Letters per Word: {}".format(avgLettersPerWord))
