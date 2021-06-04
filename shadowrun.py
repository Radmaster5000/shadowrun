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


option = intro(0)

print(option)