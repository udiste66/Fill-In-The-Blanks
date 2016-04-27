blanks  = ['__1__', '__2__', '__3__', '__4__', ]
paragraph1 = "In cuisine, an __1__ or omelet is a dish made from beaten __2__ quickly __3__ with butter or oil in a frying __4__. "
paragraph2 = "In cooking, a consomme is a type of clear __1__ made from richly flavored __2__ or bouillon that has been __3__, a process which uses __4__ whites to remove fat and sediment."
paragraph3 = '''Pressed duck is a traditional __1__ dish. The complex dish was developed in the __2__ century and consists of various parts of a duck served in a sauce of its __3__ and bone marrow, which is extracted by way of a press. It has been considered "the height of __4__." '''
answers1 = ['omelette', 'eggs', 'fried', 'pan']
answers2 = ['soup', 'stock', 'clarified', 'egg']
answers3 = ['French', '19th', 'blood', 'elegance']

#Intro
print '''Howdy Pardner! Let's play a game!'''

#The level() function will prompt a user to select a difficulty level between easy, medium and hard.
#Each choise will result in the function returning the corresponding set of paragraph and answer list, as well as printing some feedback on choice.
#If the user fails to select one of the 3 levels, even though we've tried to account for capitalisation mistakes, the function will run again from the top.
def level():
	level_choice=raw_input('Choose a difficulty level between easy, medium and hard...  ') 
	level_choice_feedback='''You have selected the difficulty level ''' + str(level_choice.lower()) + ''' try to solve the paragraph here below!'''
	level_choice_invalid='''The level you've selected is not available, please try again!''' 
	if level_choice.lower()=="easy":
		print level_choice_feedback
		return paragraph1, answers1
	elif level_choice.lower()=="medium":
		print level_choice_feedback
		return paragraph2, answers2
	elif level_choice.lower()=="hard":
		print level_choice_feedback
		return paragraph3, answers3
	else: 
		print level_choice_invalid
		return level()


#The quiz() function is the actual game, it only takes 1 input as both the paragraph and the answer list are inputs of the level() function, which we're calling inside this one. 
#The loop goes through the blanks[i] and checks if the corresponding answer matches by seeing if it equals to answer[i], if it doesn't we ask the user to try again.
#We're also counting guesses, every wrong geuss will increase this value by 1, once wronf guesses have been made the loop doesn't start due to the condition while guesses<=10 we've set. 
def quiz(blank):
	i=0
	guesses=0
	paragraph, answer = level()
	print '''You've only got 10 guesses to get this right, use them wisely!'''
	print paragraph
	while i < 4 and guesses<=10:
	    user_choice = raw_input("What should go in blank  " + blank[i] + ' ?')
	    if user_choice == answer[i]:
	        print "You got it!"
	        paragraph = paragraph.replace(blank[i],answer[i]) 
	        print paragraph 
	        i += 1
	    else:
			print 'Try again!'
			guesses=guesses+1
	else:
		print 'Too many wrong guesses mate...'


quiz(blanks)     

#Game Over
print "Thanks for playing!"