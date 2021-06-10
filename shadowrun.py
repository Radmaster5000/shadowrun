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

def mission_choice():
	print("""
	*****************************************
	           CHOOSE YOUR MISSION
	*****************************************
	
	*** FLAVOUR TEXT ABOUT MISSION CHOICE ***

		SELECT AN OPTION
		1 - Find data
		2 - Disable security

	""")
	mission = 0

	while (mission != 1 or mission != 2):
		try:
			mission = int(input('>>> '))
			if (mission == 1):
				return 'data'
			elif (mission == 2):
				return 'security'
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')


def sneak_inside(mission):
	print("""
	*****************************************
	             GET INSIDE
	*****************************************
	Current mission: """ + mission)

	print("""

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

def initial_log_in(mission):
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

	while (hack1 != 1 or hack1 != 2 or hack1 != 3):
		try:
			hack1 = int(input('>>> '))
			if (hack1 == 1 or hack1 == 2 or hack1 == 3 or hack1 == 4):
				return hack1
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def searching(mission):
	print("""
	*****************************************
	             INTEROGATE SYSTEM
	*****************************************
	
	*** FLAVOUR TEXT ABOUT SEARCHING ***

		METHODS, CHANCES, AND PENALTIES
		1 - Quick search (33% success rate)
			1 strike penalty
		2 - Moderate search (50% success rate)
			2 strike penalty
		3 - Full search (75% success rate)
			3 strike penalty""")

	hack2 = 0

	while (hack2 != 1 or hack2 != 2 or hack2 != 3):
		try:
			hack2 = int(input('>>> '))
			if (hack2 == 1 or hack2 == 2 or hack2 == 3):
				return hack2
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def task(mission):
	print("""
	*****************************************
	             TASK
	*****************************************
	
	*** FLAVOUR TEXT ABOUT TASK ***

		THIS WILL DEPEND ON TASK, SO FOR NOW:
		1 - Option 1
		2 - Option 2""")


	hack3 = 0

	while (hack3 != 1 or hack3 != 2):
		try:
			hack3 = int(input('>>> '))
			if (hack3 == 1 or hack3 == 2):
				return hack3
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def log_out(mission):
	print("""
	*****************************************
	             QUIT OUT OF SYSTEM
	*****************************************
	
	*** FLAVOUR TEXT ABOUT LOGGING OUT ***

		METHODS, CHANCES, AND PENALTIES
		1 - Rip and Tear (33% success rate)
			2 strike penalty
		2 - Calculated shutdown (50% success rate)
			1 strike penalty
		3 - Light the torch (50% success rate)
			3 strike penalty for fail
			All strikes cleared for success""")

	hack4 = 0

	while (hack4 != 1 or hack4 != 2 or hack4 != 3):
		try:
			hack4 = int(input('>>> '))
			if (hack4 == 1 or hack4 == 2 or hack4 == 3):
				return hack4
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def escape(mission):
	print("""
	*****************************************
	             GET OUT OF DODGE
	*****************************************
	
	*** FLAVOUR TEXT ABOUT LEAVING ***

		METHODS, CHANCES, AND PENALTIES
		1 - Fake it (33% success rate)
			2 strike penalty
		2 - Stealth (50% success rate)
			1 strike penalty
		3 - Guns blazing (50% success rate)
			3 strike penalty for fail
			BONUS PAYMENT FROM EMPLOYER""")

	hack5 = 0

	while (hack5 != 1 or hack5 != 2 or hack5 != 3):
		try:
			hack5 = int(input('>>> '))
			if (hack5 == 1 or hack5 == 2 or hack5 == 3):
				return hack5
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')


option = intro(0)
mission = mission_choice()
choice = sneak_inside(mission)
log_in = initial_log_in(mission)
search = searching(mission)
task_res = task(mission)
leave = log_out(mission)
run = escape(mission)

print("Intro option = " + str(option))
print("Sneak Inside option = " + str(choice))
print("Initial log in option = " + str(log_in))
print("Search option = " + str(search))
print("Task option = " + str(task_res))
print("Log out option = " + str(leave))
print("Escape option = " + str(run))