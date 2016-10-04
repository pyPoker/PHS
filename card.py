import random

deck_of_cards = [(1,'SP'),(2,'SP'),(3,'SP'),(4,'SP'),(5,'SP'),(6,'SP'),(7,'SP'),(8,'SP'),(9,'SP'),(10,'SP'),(11,'SP'),(12,'SP'),(13,'SP'),(14,'SP'),(1,'CL'),(2,'CL'),(3,'CL'),(4,'CL'),(5,'CL'),(6,'CL'),(7,'CL'),(8,'CL'),(9,'CL'),(10,'CL'),(11,'CL'),(12,'CL'),(13,'CL'),(14,'CL'),(1,'DI'),(2,'DI'),(3,'DI'),(4,'DI'),(5,'DI'),(6,'DI'),(7,'DI'),(8,'DI'),(9,'DI'),(10,'DI'),(11,'DI'),(12,'DI'),(13,'DI'),(14,'DI'),(1,'HE'),(2,'HE'),(3,'HE'),(4,'HE'),(5,'HE'),(6,'HE'),(7,'HE'),(8,'HE'),(9,'HE'),(10,'HE'),(11,'HE'),(12,'HE'),(13,'HE'),(14,'HE')]
flush_counter = 0

def copy_cards():
	return list(deck_of_cards)

def check_hand(hand):
	spades = 0
	hearts = 0
	clubs = 0
	diamonds = 0
	for x in hand:
		if x[1] == "SP":
			spades += 1
		elif x[1] == "DI":
			diamonds += 1
		elif x[1] == "HE":
			hearts += 1
		else:
		    clubs += 1
	# print("Clubs: " + str(clubs) + " Hearts: " + str(hearts) + " Diamonds: " + str(diamonds) + " Spades: " + str(spades))
	if spades is 5 or diamonds is 5 or hearts is 5 or clubs is 5:
		global flush_counter 
		flush_counter += 1
		#print("FLUSH BRUH")

def main():
	deck = copy_cards()
	for x in xrange(1,100000):
		hand_results = []
		for x in range(0,7):
		    random.shuffle(deck)
		    result = random.choice(deck)
		    deck.remove(result)
		    hand_results.append(result)
		check_hand(hand_results)
		deck = copy_cards()
	global flush_counter
	print("Flush: " + str(flush_counter))

if __name__ == '__main__':
    main()