from __future__ import division
import random
from operator import itemgetter, attrgetter


deck_of_cards = [(2,'SP'),(3,'SP'),(4,'SP'),(5,'SP'),(6,'SP'),(7,'SP'),(8,'SP'),(9,'SP'),
(10,'SP'),(11,'SP'),(12,'SP'),(13,'SP'),(14,'SP'),(2,'CL'),(3,'CL'),(4,'CL'),(5,'CL'),
(6,'CL'),(7,'CL'),(8,'CL'),(9,'CL'),(10,'CL'),(11,'CL'),(12,'CL'),(13,'CL'),(14,'CL'),
(2,'DI'),(3,'DI'),(4,'DI'),(5,'DI'),(6,'DI'),(7,'DI'),(8,'DI'),(9,'DI'),(10,'DI'),
(11,'DI'),(12,'DI'),(13,'DI'),(14,'DI'),(2,'HE'),(3,'HE'),(4,'HE'),(5,'HE'),(6,'HE'),
(7,'HE'),(8,'HE'),(9,'HE'),(10,'HE'),(11,'HE'),(12,'HE'),(13,'HE'),(14,'HE')]

royal_flush_counter = 0
straight_flush_counter = 0
four_of_a_kind = 0
full_house_counter = 0
flush_counter = 0
straight_counter = 0
three_of_a_kind = 0
two_pair_counter = 0
pair_counter = 0
high_card_counter = 0

def copy_cards():
	return list(deck_of_cards)

def check_hand(hand):
	spades = 0
	hearts = 0
	clubs = 0
	diamonds = 0
	sorted_hand = sorted(hand, reverse=True)
	is_a_straight = True
	ahead_works = True
	behind_works = True
	ahead = 1
	behind = 1
	straight_count = 1
	loop_counter = 0
	straight_deck = []
	straight_deck.append(sorted_hand[3])
	while is_a_straight:
		if loop_counter <= 4:
			if behind_works:
				if behind <= 3:
					# print("Is " + str(sorted_hand[3][0]) + " == " + str(sorted_hand[(3-behind)][0] - behind))
					if sorted_hand[3][0] is (sorted_hand[(3-behind)][0] - behind):
						
						straight_count += 1
						# print(sorted_hand[(3-behind)])
						# print(sorted_hand[3-behind])
						# print(len(sorted_hand))
						# print("Index " + str(3-behind))
						straight_deck.append(sorted_hand[(3-behind)])
						behind += 1
						# print("BEHIND")
					else:
						behind_works = False
			if ahead_works:
				if ahead <= 3:
					# print("Is " + str(sorted_hand[3][0]) + " == " + str(sorted_hand[(3+ahead)][0] + ahead))
					if sorted_hand[3][0] is (sorted_hand[(3+ahead)][0] + ahead):
						
						straight_count += 1
						# print("Ahead is: " + str(ahead))
						# print(sorted_hand[(3+ahead)])
						# print(len(sorted_hand))
						# print("Index " + str(3+ahead))
						straight_deck.append(sorted_hand[(3+ahead)])
						ahead += 1
						# print("AHEAD")
					else:
						ahead_works = False
			if ahead_works is False and behind_works is False:
				is_a_straight = False
			if straight_count is 5:
				pass
			loop_counter += 1
		else:
			# is_a_straight = False
			break
	if is_a_straight:
		sorted_hand = sorted(straight_deck, reverse=True)

	for x in sorted_hand:
		if x[1] == "SP":
			spades += 1
		elif x[1] == "DI":
			diamonds += 1
		elif x[1] == "HE":
			hearts += 1
		else:
		    clubs += 1
	
	is_a_flush = False
	#print("Spades: " + str(spades) + " Hearts: " + str(hearts) + " Clubs: " + str(clubs) + " Diamonds: " + str(diamonds))
	if spades >= 5 or diamonds >= 5 or hearts >= 5 or clubs >= 5:
		is_a_flush = True
	if is_a_straight:
		if is_a_flush:
			global straight_flush_counter
			straight_flush_counter += 1
			print("STRAIGHT FLUSH")
		else:
			global straight_counter 
			straight_counter += 1
			print("STRAIGHT")
	elif is_a_flush:
		global flush_counter 
		flush_counter += 1
		print("FLUSH")
	

	
		

def run_test():
	deck = [(2,'HE'),(3,'HE'),(10,'HE'),(11,'HE'),(12,'HE'),(13,'HE'),(14,'HE')]
	print("Should be: Royal Flush")
	check_hand(deck)

	deck = [(2,'HE'),(3,'HE'),(4,'HE'),(5,'HE'),(6,'HE'),(7,'HE'),(8,'HE')]
	print("Should be: Straight Flush")
	check_hand(deck)
	

	deck = [(2,'HE'),(2,'CL'),(4,'HE'),(5,'CL'),(6,'HE'),(7,'HE'),(8,'CL')]
	print("Should be: Straight")
	check_hand(deck)
	

	deck = [(10,'HE'),(2,'CL'),(4,'CL'),(9,'CL'),(6,'CL'),(7,'HE'),(11,'CL')]
	print("Should be: Flush")
	check_hand(deck)
	


def run_loop():
	deck = copy_cards()
	for x in xrange(1,100):
		hand_results = []
		for x in range(0,7):
		    random.shuffle(deck)
		    result = random.choice(deck)
		    deck.remove(result)
		    hand_results.append(result)
		check_hand(hand_results)
		deck = copy_cards()
	global flush_counter
	global straight_counter
	percent_flush = flush_counter / 100000
	percent_straight = straight_counter / 100000
	print("Flush: " + str(flush_counter) + " Percent: " + str(percent_flush) + " Straights: " + str(straight_counter) + " Percent: " + str(percent_straight))

def main():
	#run_loop()
	run_test()

if __name__ == '__main__':
    main()