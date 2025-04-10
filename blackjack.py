import random

def black_jack():
    
    deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    dealers_hand = []
    players_hand = []
    game_status = "play"
    deck_index = 0
    user_input = " "
    

    def draw_card():
        deck_index = len(deck_of_cards) - 1
        card_index = random.randint(0, deck_index)
        #print(card_index)
        
        card = deck_of_cards[card_index]
        #print(card)
        
        deck_of_cards.pop(card_index)
        #print(len(deck_of_cards))
        
        return card
        
    def add_to_player():
        card_to_add = draw_card()
        players_hand.append(card_to_add)

        if len(players_hand) > 1:
            print("Player draws a: " + str(card_to_add))

    def add_to_dealer():
        card_to_add = draw_card()
        dealers_hand.append(card_to_add)
        if len(dealers_hand) > 1:
            print("Dealer draws a: " + str(card_to_add))

    def start_game():
        add_to_player()
        add_to_dealer()
        
    
    def check_hand(name_of_player, hand):
        checking_hand = hand
        
        j = "J"
        q = "Q"
        k = "K"
        a = "A"

        number_of_As = 0
        number_of_cards_over_10 = 0
        i = 0

        
        for card in checking_hand:
            if 'J' == card:
                checking_hand[i] = 10
                number_of_cards_over_10 = number_of_cards_over_10 + 1

            elif 'Q' == card:
                checking_hand[i] = 10
                number_of_cards_over_10 = number_of_cards_over_10 + 1

            elif 'K' == card:
                checking_hand[i] = 10
                number_of_cards_over_10 = number_of_cards_over_10 + 1
            
            elif 'A' == card:
                number_of_As = number_of_As + 1
                checking_hand.remove(card)
             
            i = i + 1
        
        sum_of_hand = sum(checking_hand)


        sum_11 = sum_of_hand + (number_of_As * 11)
        sum_1 = sum_of_hand + (number_of_As * 1)
        
        if number_of_As > 0:
            
            print("If A = 11: " + str(sum_11))
            print("If A = 1: " + str(sum_1))

        else:
            print(sum_of_hand)
        
        if number_of_As > 0 and number_of_cards_over_10 > 0:
            game_status = "winner"
            print(name_of_player + " is the winner")

        if (sum_11) > 21 or (sum_1) > 21:
            game_status = "loser"
            
        print(game_status)
        
       # print(sum_of_hand)

    def player_draw_card():
        
        while game_status == "play":
            print("---------------------------------------------------------------------")
            user_input = input("Do you want to draw another card? (Enter 'y' for yes and 'n' for no):")
            print("---------------------------------------------------------------------")
            print(" ")
            if user_input == "y":
                add_to_player()
                print('Your Hand: ' + str(players_hand))
                print(" ")
                check_hand("Player", players_hand)
                add_to_dealer()
                print("Dealer's Hand: " + str(dealers_hand))
                print(" ")
                check_hand("Dealer", dealers_hand)
                

                
            if user_input == "n":
                add_to_dealer()
                print(" ")
                print('Your Hand: ' + str(players_hand))
                check_hand("Player", players_hand)
                print("Dealer's Hand: " + str(dealers_hand))
                check_hand("Dealer", dealers_hand)
                
        if game_status == "winner":
            print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print("Welcome to a digital version of Black Jack! Let's get this game started!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")
    start_game()

    while game_status == "play":
        print("Your card(s):" + str(players_hand))
        print("Dealers card(s):" + str(dealers_hand))
        print(" ")
        player_draw_card()
    


    

black_jack()       
