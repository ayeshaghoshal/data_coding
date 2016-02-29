# -*- coding: utf-8 -*-

print "Cinderella's nightmare ball"

from sys import exit

def ballroom():
	print """Cinderella is in the ballroom! Now to find her prince! \n
	Who does she you ask about the prince? His mother, the ugly sisters or the king?"""
		
	ask = raw_input("> ")
	
	if "mother" in ask:
		print "Cinderella is politely escorted to the door, never to be seen again. Tough luck for cinderella!"
		
	elif "ugly" in ask:
		print "Cinderella is dragged home and locked up never to be seen again. Poor child!"
		
	elif "king" in ask:
		print "Cinderella is reunited with her prince and they live happily ever after!"
		exit(0)
	else:
		print "Tough luck kid!"
			

def attic():
	print """Cinderella is led to the top of the mansion and left outside a wooden door \n
	She enters the room which is an attic \n
	A hooded figure comes up behind her and locks her up in a cage \n
	It asks - I need x amount of gold coins. Pay me and be free. (Enter a number)"""
	
	ask = raw_input("> ")
	
	if ask.isdigit():
		how_much = int(ask)
	else:
		print "Please type a number!!"
		
	if how_much in range(100, 5000):
		print "Mmmm, you are one wealthy babe! I might just kidnap you for ransom!! *Cackle*"
		exit(0)
	elif 50 < how_much < 99:
		ballroom()
	elif how_much < 50:
		print "You are such a pauper! I have no use for you. You die."
	else:
		print "I am going to eat you alive!"

def basement():
	print "Cinderella slips past the guards and arrives in a cold dark basement. At least the guards aren't chasing her!"
	print "She comes across a notorius murderer chained up inside."
	print "The prisioner tells her he can get her to the ballroom if he lets her out with the axe at the other side of the room."
	print "What should cinderella do? Should she help the murderer or leave the basement to be met with the mansion guards."
	
	ask = raw_input("> ")
	
	if "help" in ask: # automatically moves onto the next elif even though the words don't match with the elif.
		print "Thank you Child. I am actually the Mayor of this town and was wrongly imprisoned. I will lead you to the Ballroom."
		ballroom()
	elif "leave" in ask:
		print "Cinderella is met with 10 mansion guards and she is dragged to the attic and locked up."
		attic()
	else:
		print "Cinderella gets trapped in the basement with the murderer for all eternity!"


def mansion():
	print """This is the story of Cinderella and her plight to reunite with her prince Charming. her fate is in your hands! No pressure.
	"Our story starts when she arrives at the door of the price's palacial mansion
	The mansion butler, who was given strict instructions not to let Cinderella in, opens the door.
	The butler asks, Who are you here to see?"""
	bad_mood = True
	
	ask = raw_input("> ")
	
	if ask == "prince" and bad_mood:
		print "The prince is not expecting any guests today!! Guards! Capture her!."
		basement()
		bad_mood = False # how does this alternate level of mood factors in??
	elif ask == "prince" or bad_mood:
		print "You may proceed to the ballroom. Only because I am in a good mood!"
		ballroom()
	else:
		attic()
	

mansion()










	
