 
#Problem 2: Adventure Game Updates
#Use showInformation to pop up a welcome box at the beginning that explains your game. 
 #In the main game loop I added this line when the game starts.
    showInformation("Welcome to Jailbreak\n You are a prisoner who is looking to escpae from one of the most dangerous prisons in the world.\n")
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())

#Think about other places where a dialog box might be better than the console.#I did a pop up dialogue box when you type in exit. 
 # handle a request to exit
        if input == 'exit':
          showInformation('Are you really going to give up that easy.')
          break
#Use a mix of the two types of output - use your judgment to decide how to use the different types. 
#Was not sure what they meant when they put different types. So I just did two outputs using the showInformation


#Add Strings
#At the beginning of your game, ask the user to enter their name (or to name their character). 
 # Main game loop
    showInformation('Welcome to Jailbreak\n You are a prisoner who is looking to escpae from one of the most dangerous prisons in the world.\n')
    name = requestString('Please type in your characters name')
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())

#Use the user's name at least one other place in your program (maybe when they win or lose!). 
# for this I put the users name to appear when you win in the Secret room. We can change this but just what I did.
	  # secret room
        if player1.getLocation() == room10 and 'lockpick' in player1.getInventory():
            printNow(player1.getLocation().getName())
            printNow(player1.getLocation().getDesc())
            printNow('You use the lockpick on the strange keyhole.')
            printNow('You found a secret exit ' + name + '. You win!!!')  
            gameWon = True 
            

#Addlist
#Now that we've explored lists, you can probably think of multiple ways to use them in your adventure game. 
#In particular, lists should really help you cut down on the number of global variables you need since you can have a single list 
#for inventory or to hold other important information.  
#Go back through your adventure game and think about whether there is an opportunity to use lists to simplify your code.  
#Created a list for our inventory
Inventorylist = ['key', 'lockpick', 'cat'] # here is my list of the items we have in the game

if 'key' in Inventorylist:# I did if statements to check if have their item in the Invenotrylist but I am not sure this is the right way to do it.
  print('You have a key in your inventory')
elif 'lockpick' in Inventorylist:
  print('You have a lockpick in your inventory')
else:    
  print('You have a cat in your inventory')
 

  