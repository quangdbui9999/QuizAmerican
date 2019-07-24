import random # random the countries and capitals
import operator # using to sort the Capitals of Dictionany
from pathlib import Path # Using to check the file is existed.

def inputFile():
    print('Enter the File Name:')
    inFile = input()
    return inFile

def readFileToDictionary(inFileName, inDiction):
    readFile = open(inFileName)

    with readFile as element:
        for line in element:
            ''' strip(): the combination of lstrip() and rstrip(), it will create a new string,
            delete the space at the beginning and the end of string, it also remove tab, new line '''
            ''' split(None, 1): None is the same with character ' '. The second pararameter is mean
            Example the string 'Quang Bui CSC' (Key: 'Quang', Value: 'Bui CSC')
            1: 'Quang', 'Bui CSC'     '''
            keyCountry, valueCapital = line.strip().split(":", 1)
            inDiction[keyCountry] = valueCapital.strip()
    readFile.close()

def inputFromUser(nameCountry):
    print('\nWhat is the capital of \"' + nameCountry + '\"?')
    print('My Capital City is: ')
    userAnswer = input()
    return userAnswer

def reportInformation(inScore, inPercent_correct):
  print('THE END OF GAME.')
  print('Your score is: ' + str(inScore))
  print('Your percent correctly is: ' + str(round(inPercent_correct, 2)) + '%')

def sortedValueDictionary(inDictionCountry):
    countSorted = 0

    '''
    sortedCapital is a list of tuples. Each tuple contains the key and value
    for each item found in the dictionary. The second element of tuple is sorted.
    '''
    print('\nList of the countries with their capital cities (sorted alphabetically)')
    sortedCapital = sorted(inDictionCountry.items(), key=operator.itemgetter(1))
    for valueSorted in sortedCapital:
        countSorted = countSorted + 1
        print(str(countSorted) + ": " + str(valueSorted))

# oldDictCountry: myDictionCountry diction read from FileExistsError
# newDictCountry: store the new diction after each correct answer by update() method and sorted by capital
# counter: how many loop to run?
# inScore: 1 point after each correct ansnwer
# inPercentCorrect: the percent of correct answer, used in reportInformation() method
def compareAnswer(oldDictCountry, newDictCountry, counter, inScore, inPercentCorrect):
    while len(oldDictCountry) >= 1:
        country, capital = random.choice(list(oldDictCountry.items()))
        playerAnswer = inputFromUser(country)
        counter = counter + 1

        if capital.lower() == playerAnswer.lower():
            print('\nYour answer is CORRECT!')
            inScore = inScore + 1
            newDictCountry.update({country:capital})
            del oldDictCountry[country]
        else:
            print('\nYour answer is INCORRECT!')
            print('The RIGHT ANSWER is: ' + capital)
        
        inPercentCorrect = (inScore / counter) * 100
        
        count = 0;
        if len(oldDictCountry) != 0:
            print('\nList of the ' + str(len(oldDictCountry)) + " is:")
            for eachKey in oldDictCountry:
                count = count + 1
                print(str(count) + ": " + eachKey)
    sortedValueDictionary(newDictCountry)
    reportInformation(inScore, inPercentCorrect)

def listNameCountry(inDictionCountry):
    arrCountry = [] # store the name of the Country
    # Convert the keys in myDictionCountry into an array
    for keyDiction in inDictionCountry.keys():
        arrCountry.append(keyDiction)
    # Shuffle the array
    random.shuffle(arrCountry)

    count = 0
    # Output the element of each country in the random
    for key in arrCountry:
        count = count + 1
        print(str(count) + ". " + key)
    print('\nThere are ' + str(len(inDictionCountry)) + ' countries in South America.')

def listNameCapital(inDictionCountry):
    arrCapital = [] # store the name of the Capital
    # Convert the values in myDictionCountry into an array
    for value in inDictionCountry.values():
        arrCapital.append(value)
    # Shuffle the array
    random.shuffle(arrCapital)

    count = 0
    print('\n\nThe name of capitals')
    for value in arrCapital:
        count = count + 1
        print(str(count) + ". " + value)
    print('\nThere are ' + str(len(inDictionCountry)) + ' capitals in South America.')


myDictionSouthAmerica = {}
fileName = inputFile();
existFile = Path(fileName)
if(existFile.is_file()):
    readFileToDictionary(fileName, myDictionSouthAmerica)

    print('The name of each Country:')
    listNameCountry(myDictionSouthAmerica)
    listNameCapital(myDictionSouthAmerica)
    
    score = 0 # 1 score for each question is correct
    percent_correct = 0.0 # increamenting to 1 for each question is correct
    repeat_loop = 0 # the incremented, the repeat_loop will increament to 1 after each while loop
    newDictionSouthAmerica = {} # the temp of dictionary

    compareAnswer(myDictionSouthAmerica, newDictionSouthAmerica, repeat_loop, score, percent_correct)
else:
    print('File name: \"' + fileName + '\" does not exist.')
