import os 
import re
# function to calculate avg
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

class Paragraph():
    def __init__(self, data, number):
        self.data = data
        self.number = number

    def analysis(self):
        paragraph_txt = os.path.join(self.data)
        sentence_re = re.compile(r"(?:[.!?])|(?:\n|\n\r:) +", re.MULTILINE)
        with open(paragraph_txt, 'r') as p_file:
            paragraph = p_file.read()

        wordList = paragraph.split(" ")
        wordCount = len(wordList)
        sentenceList =  re.split(sentence_re, paragraph)
        sentenceCount = len(sentenceList)
        avgWordsPerSentence = mean([len(sentence.split(" ")) for sentence in sentenceList])
        avgLettersPerWord = mean([len(word) for word in wordList])
        print("Paragraph Analysis #" + str(self.number))
        print("-")*50
        print("Word Count: {}".format(wordCount))
        print("Sentence Count: {}".format(sentenceCount))
        print("Average Words per Sentence: {}".format(avgWordsPerSentence))
        print("Average Letters per Word: {}".format(avgLettersPerWord))
        print("*")*50
#########################################################################################
p1 = Paragraph('paragraph_1.txt', 1)
p2 = Paragraph('paragraph_2.txt', 2)

p1.analysis()
p2.analysis()
