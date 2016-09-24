import random

deck_of_cards = [(1,'SP'),(2,'SP'),(3,'SP'),(4,'SP'),(5,'SP'),(6,'SP'),(7,'SP'),(8,'SP'),(9,'SP'),(10,'SP'),(11,'SP'),(12,'SP'),(13,'SP'),(14,'SP'),(1,'CL'),(2,'CL'),(3,'CL'),(4,'CL'),(5,'CL'),(6,'CL'),(7,'CL'),(8,'CL'),(9,'CL'),(10,'CL'),(11,'CL'),(12,'CL'),(13,'CL'),(14,'CL'),(1,'DI'),(2,'DI'),(3,'DI'),(4,'DI'),(5,'DI'),(6,'DI'),(7,'DI'),(8,'DI'),(9,'DI'),(10,'DI'),(11,'DI'),(12,'DI'),(13,'DI'),(14,'DI'),(1,'HE'),(2,'HE'),(3,'HE'),(4,'HE'),(5,'HE'),(6,'HE'),(7,'HE'),(8,'HE'),(9,'HE'),(10,'HE'),(11,'HE'),(12,'HE'),(13,'HE'),(14,'HE')]


for x in range(0,7):
    # print("Rank: " + random.choice(rank) + " suit: " + random.choice(suit))
    random.shuffle(deck_of_cards)
    result = random.choice(deck_of_cards)
    deck_of_cards.remove(result)
    print(result)
