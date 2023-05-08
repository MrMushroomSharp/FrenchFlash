from bs4 import BeautifulSoup
import requests
import random
import threading
import time

print("Loading...\n\n")

pageToScrape = requests.get('https://1000mostcommonwords.com/1000-most-common-french-words/')
soup = BeautifulSoup(pageToScrape.text, "html.parser")
quotes = soup.findAll('td')

listNumber = 1
listCycle = 0

frenchWords = []
englishWords = []
numberList = []

# Organize the scraped data/words
for quote in quotes:
    # Ignore the first three text elements since it is unnecessary
    if listNumber == 1 or listNumber == 2 or listNumber == 3:
        listNumber += 1
    # Organize each word and number into their corresponding list
    else:
        if listCycle == 0:
            numberList.append(quote.text)

        elif listCycle == 1:
            frenchWords.append(quote.text)

        elif listCycle == 2:
            englishWords.append(quote.text)
            listCycle = -1

        listCycle += 1


def StartGame():
    translateMode = transMode
    wordCount = 0
    while gameRunning:
        if translateMode == '1':
            randomWord = random.randint(0, 1000)
            ans = input("\nWhat does " + frenchWords[randomWord] + " Mean? ")

            if ans == englishWords[randomWord]:
                print("Correct!")
                wordCount += 1
            elif ans == '?1':
                print("That answer is " + englishWords[randomWord])
            elif ans == '?2':
                print("That answer is " + englishWords[randomWord])
            else:
                print("Sorry that is incorrect, the answer is " + englishWords[randomWord])

        elif translateMode == '2':
            randomWord = random.randint(0, 1000)
            ans = input("\nWhat is " + englishWords[randomWord] + " in French? ")

            if ans == frenchWords[randomWord]:
                print("Correct!")
                wordCount += 1
            elif ans == '?1':
                print("That answer is " + frenchWords[randomWord])
            elif ans == '?2':
                print("That answer is " + frenchWords[randomWord])
            else:
                print("Sorry that is incorrect, the answer is " + frenchWords[randomWord])

        elif translateMode == '3':
            randomMode = random.randint(0, 2)
            if randomMode == 0:
                translateMode = '1'
            else:
                translateMode = '2'


input("Welcome to French Flash! A flashcard deck of the top 1000 most common french words to help increase your "
      "french vocabulary! ")

game = input("\n\nDo you want to play a normal game(n) or you weak words deck(w): ")

gameRunning = True
if game == 'n':
    transMode = input("Would you like to play with French to English (1), English To French (2), Or Both (3): ")
    gameTime = input("How much time would you like 1-10 minutes: ")

    t = threading.Thread(target=StartGame)
    t.start()
    time.sleep(int(gameTime)*60)
    print("\n\nYour time is up! Hope you had a fun time! Click enter to leave.\n\n")
    gameRunning = False
    t.join()
