import time

# Creating the Intro screen

def intro(key):

	# repeats until player presses 1, 2, or 3
	while (key != 1 or key != 2 or key != 3):

		print("""

	#### #  # #### ###  #### #     # #### #  # #   #
	#    #  # #  # #  # #  # #     # #  # #  # ##  #
	#### #### #### #  # #  # #  #  # #### #  # # # # 
	   # #  # #  # #  # #  # # # # # # #  #  # #  ##
	#### #  # #  # ###  #### ### ### #  # #### #   #

	     		Welcome to Shadowrun!
	Take the role of a Decker and choose your run!

	************************************************

			SELECT AN OPTION:
			1 - Start game
			2 - How to play
			3 - Quit

	************************************************
		   """)

		try:
			key = int(input('>>> '))
			if (key == 1):
				return 1
			elif (key == 2):
				rules()
			elif (key == 3):
				quit()
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')


# selection 2 from the introduction screen
def rules():
	print("""
	*****************************************
			RULES AND STUFF
	*****************************************
	""")

	print("TODO: write the rules")
	print()
	choice = input("	When you're ready, type 'back' to continue...")
	if (choice == 'back'):
		return
	else:
		print()
		print()
		print("That's not the word 'back', is it?...")
		print()
		print()
		time.sleep(1)
		rules()

def sneak_inside():
	print("""
	*****************************************
	             GET INSIDE
	*****************************************
	
	*** FLAVOUR TEXT ABOUT SNEAKING IN ***

		SELECT AN OPTION
		1 - Sneak past guard
		2 - Take down guard

	""")

	choice = 0

	while (choice != 1 or choice != 2):
		try:
			choice = int(input('>>> '))
			if (choice == 1 or choice == 2):
				return choice
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def initial_log_in():
	print("""
	*****************************************
	             COMPROMISE SYSTEM
	*****************************************
	
	*** FLAVOUR TEXT ABOUT LOGGING IN ***

		SELECT AN OPTION
		1 - Brute force password
		2 - Use professional crypto program
		3 - Use custom program""")
	if (choice == 2):
		print("		4 - Use guard's details (HIDDEN)")

	hack1 = 0

	while (hack1 != 1 or hack1 != 2):
		try:
			hack1 = int(input('>>> '))
			if (hack1 == 1 or hack1 == 2 or hack1 == 3 or hack1 == 4):
				return hack1
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')



option = intro(0)
choice = sneak_inside()
log_in = initial_log_in()

print("Intro option = " + str(option))
print("Sneak Inside option = " + str(choice))
print("Initial log in option = " + str(log_in))