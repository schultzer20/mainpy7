import nltk
from nltk.corpus import wordnet
from nltk.corpus import names
import random

# nltk.download('wordnet')
# nltk.download('names')


def generate_names(char, num):
    if char in [chr(i) for i in range(97, 123)]:
        x = char.upper()
        female_names = names.words('female.txt')
        male_names = names.words('male.txt')

        filtered_females = []
        for name in female_names:
            if name.startswith(x):
                filtered_females.append(name)

        filtered_male = []
        for name in male_names:
            if name.startswith(x):
                filtered_male.append(name)

        if len(filtered_females) == 0:
            return "No female names with the letter ", char, "."
        if len(filtered_male) == 0:
            return "No male names with the letter ", char, "."

        female_list = random.choices(filtered_females, k=num)
        male_list = random.choices(filtered_male, k=num)

        gender_f = [(name, "female") for name in female_list]
        gender_m = [(name, "male") for name in male_list]

        textfile1 = open("female_names.txt", "w")
        for element in female_list:
            textfile1.write(element + "\n")
        textfile1.close()

        textfile2 = open("male_names.txt", "w")
        for element in male_list:
            textfile2.write(element + "\n")
        textfile2.close()

        print(gender_f)
        print(gender_m)
        return ""

    else:
        return "Wrong input. Enter a letter."


print(generate_names("w", 9))


class SynAnt:
    def __init__(self, word_list):
        self.word_list = word_list
        syns = wordnet.synsets()

    def find_synonyms(self):
        synonyms = []
        for syn in wordnet.synsets():
            for l in syn.lemmas():
                synonyms.append(l.name())
            if len(synonyms) == 0:
                synonyms.append("No synonyms found.")
            else:
                print(set(synonyms))

    def find_antonyms(self):
        antonyms = []
        for syn in wordnet.synsets():
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms([0].name()))
            if len(antonyms) == 0:
                antonyms.append("No antonyms found")
            else:
                print(set(antonyms))
