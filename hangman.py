import random
import sys
wordOptions = ['apple', 'banana', "insert", "your", "words", "in", "this", "python", "list", "please", "help", "goat", "rainbow","cheese", "heaven", "music", "train", "danger", "long", "alphabet", "brain", "chair", "surf", "cat", "zoo", "sweet", "brother", "sister"]
count = 0



def theGallow(count):
    if count == 0:
        print('_______')
        print('|     |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----')
    elif count == 1:
        print('_______')
        print('|     |')
        print('|     o')
        print('|')
        print('|')
        print('|')
        print('----')
    elif count == 2:
        print('_______')
        print('|     |')
        print('|     o')
        print('|     |')
        print('|')
        print('|')
        print('----')
    elif count == 3:
        print('_______')
        print('|     |')
        print('|     o')
        print('|    /|')
        print('|')
        print('|')
        print('----')
    elif count == 4:
        print('_______')
        print('|     |')
        print('|     o')
        print('|    /|\ ')
        print('|')
        print('|')
        print('----')

    elif count == 5:
        print('_______')
        print('|     |')
        print('|     o')
        print('|    /|\ ')
        print('|     |')
        print('|')
        print('----')
    elif count == 6:
        print('_______')
        print('|     |')
        print('|     o')
        print('|    /|\ ')
        print('|     |')
        print('|    /')
        print('----')
    elif count == 7:
        print('_______')
        print('|     |')
        print('|     o')
        print('|    /|\ ')
        print('|     |')
        print('|    / \ ')
        print('----')
        print('YOU LOST!')



def nextGo(guessedLetters,letterList, doneLetters, count):
    
    while count < 7:
        if '_' in guessedLetters:
            print('Guess another letter/word:')
            z = input()
            if z == randomWord:
                print('Yes! ' + z + ' is the word, well done!')
                sys.exit()
            elif z in doneLetters:
                print('You have guessed that one already.')
                print(' '.join(guessedLetters))
                nextGo(guessedLetters,letterList, doneLetters, count)
            elif len(z) > 1:
                print('That is not the word.')
                count += 1
                theGallow(count)
                print(' '.join(guessedLetters))
                nextGo(guessedLetters,letterList, doneLetters, count)
            elif z in letterList:
                print('Good job. That letter is in the word!')
                doneLetters.append(z)
                for i in letterList:
                    if i == z:
                        place = letterList.index(i)
                        guessedLetters[place] = i
                        letterList[place] = '1'
                print(' '.join(guessedLetters))

                nextGo(guessedLetters,letterList, doneLetters, count)
            else:
                print('Wrong')
                doneLetters.append(z)
                count += 1
                theGallow(count)
            
        else:
            count = 10
            print('You win!!')
            sys.exit()
            
   

def hangMan():
    count = 0
    print('Guess a letter/word:')
    z = input()
    letterList = []
    doneLetters = []
    guessedLetters = []
    for i in randomWord:
        letterList.append(i)
    if z == randomWord:
        print('Yes! ' + z + ' is the word, well done!')
        sys.exit()
    elif len(z) > 1:
        print('That is not the word.')
        count += 1
        theGallow(count)
        print(' '.join(guessedLetters))
        for i in letterList:
            guessedLetters.append('_')
        nextGo(guessedLetters,letterList, doneLetters, count)
    elif z in letterList:
        print('Good job. That letter is in the word!')
        doneLetters.append(z)
        
        for i in letterList:
            if i == z:
                guessedLetters.append(i)
            else:
                guessedLetters.append('_')
        
        print(' '.join(guessedLetters))
        nextGo(guessedLetters, letterList, doneLetters, count)
        
  
    else:
        print('Wrong')
        count += 1
        theGallow(count)
        doneLetters.append(z)
        for i in letterList:
            guessedLetters.append('_')
        print(' '.join(guessedLetters))
        nextGo(guessedLetters, letterList, doneLetters, count)
    

      
print('Would you like to play Hangman (Y or N)?' )
x = input()

if x == 'Y':
    
    theGallow(0)
    randomWord = random.choice(wordOptions)
    y = len(randomWord)
    print('The word has ' + str(y) + ' letter(s)')
    print(y * '_ ')
    hangMan()
    
elif x == 'N':
    print('No worries.')
else:
    print('I can only process "Y" or "N" answers')


