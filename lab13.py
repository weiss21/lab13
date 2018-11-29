#Step 1: Find a news article online
#You only need between 100 and 200 words for a decent mad lib, so if you find a really long story, take only part of it.  
#Step 2: Remove some words
#Go through the article and turn it into strings in Python and remove some of the words.  These will be the words that become part of the Mad Lib Game
myList = ['There was no doubt that my', 'pets', 'had to be included in my','wedding','\
.I am so obsessed with them. I walked down the', 'aisle', 'first so that I would be on \
the stage to watch Toby and Rooby go down. They were the main focus and the reason I chose my \
','amazing venue','.There was no negotiating. The ','dogs', 'had to be a huge part of my wedding. They are my', \
'kids','.Toby had a custom tuxedo made with gold buttons and velvet accents which was modeled after the','grooms','.Roobys\
dress was modeled after Sarah Jessica Parkers outfit in the opening of Sex and the City.']
myList.remove('pets')
myList.remove('wedding')
myList.remove('aisle')
myList.remove('amazing venue')
myList.remove('dogs')
myList.remove('kids')
myList.remove('grooms')
myList


#Step 3: Make some design decision
#You need to think about how you are going to ask the user to enter the words, how you are going to store the words entered, 
#and how you are going to print out the restulting story.  There are several different ways to accomplish this using strings and lists.  
#The one rule is that you cannot use a separate variable for every word you need.

#Step 4: Collect words from the user
#Prompt the user to enter the words that you need to fill in your mad lib 

# just an idea, the type of words you need to fill in could be another list
wordsNeeded = ['plural noun', 'event', 'place', 'place', 'plural animal', 'plural noun', 'plural noun']

# then you can collect their madlib words with a loop. collect all the answers in a list for later.
solutionList = []
for word in wordsNeeded:
  answer = requestString('Please type in a %s' % word)
  solutionList.append(answer)

#Step 5: Print the results
#Combine the original text plus the new words to print your final mad lib.   

  
#Problem 2: Adventure Game Updates
#Use showInformation to pop up a welcome box at the beginning that explains your game. 
 #In the main game loop I added this line when the game starts.
    showInformation("Welcome to Jailbreak\n You are a prisoner who is looking to escpae from one of the most dangerous prisons in the world.\n")
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())

#Think about other places where a dialog box might be better than the console. 
 # handle a request to exit
        if input == 'exit':
          showInformation("Are you really going to give up that easy..")
          #printNow('Quitting game. Have a nice day.')
          break
#Use a mix of the two types of output - use your judgment to decide how to use the different types.

#Add Strings
#At the beginning of your game, ask the user to enter their name (or to name their character). 
 # Main game loop
    showInformation('Welcome to Jailbreak\n You are a prisoner who is looking to escpae from one of the most dangerous prisons in the world.\n')
    name = requestString('Please type in your characters name')
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())

#Use the user's name at least one other place in your program (maybe when they win or lose!).
	  # secret room
        if player1.getLocation() == room10 and 'lockpick' in player1.getInventory():
            printNow(player1.getLocation().getName())
            printNow(player1.getLocation().getDesc())
            printNow('You use the lockpick on the strange keyhole.')
            printNow(name)
            printNow('You found a secret exit. You win!!!')  
            gameWon = True 
 

##Add Lists
#Now that we've explored lists, you can probably think of multiple ways to use them in your adventure game. 
#In particular, lists should really help you cut down on the number of global variables you need since you can have a single list for inventory or to hold other important information.  
#Go back through your adventure game and think about whether there is an opportunity to use lists to simplify your code.  

  