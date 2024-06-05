import random

class DeckOfCards:
    
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
        self.names = {'2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', 'Jack': 'Jack', 'Queen': 'Queen', 'King': 'King', 'Ace': 'Ace'}
        self.deck = [(value, name, suit) for value, name in self.names.items() for suit in self.suits]


class Dealer(DeckOfCards):

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    def draw_card(self):
        if not self.deck:
            return None  # Return None if the deck is empty
        return self.deck.pop()
    
    def double_deal(self): 
        first_hand = []
        for i in range(2):
            first_hand.append(self.draw_card())
        return first_hand 
    

class Players(Dealer):

    def __init__(self):
        super().__init__

    def take_first_cards(self):
        player_hand = dealer.double_deal()
        return player_hand
    
    def twist(self, player_hand):
        another_card = dealer.draw_card()
        player_hand.append(another_card)
        return player_hand
    
    def total_score(self, player_hand, score_list):
        for i in range(len(player_hand)):
            if player_hand[i][0] == "Ace":
                if sum(score_list) < 11:
                    score_list.append(11)
                else:
                    score_list.append(1)
            elif player_hand[i][0] == "Jack":
                score_list.append(10)
            elif player_hand[i][0] == "Queen":
                score_list.append(10)
            elif player_hand[i][0] == "King":
                score_list.append(10)
            else:
                score_list.append(int(player_hand[i][0]))
        return score_list
    


class Display():

    def display_hand(self, hand):
        print("\nYour Hand:")
        for i in range(len(hand)):
            print(f"The {hand[i][0]} of {hand[i][2]}")
    
    def display_score(self, score):
        print(f"\nScore: {score}\n")


    
deck_of_cards = DeckOfCards()
dealer = Dealer()
players = Players()
display = Display()
print("\nWelcome to the Black Jack Table\n"
      "Here are your first cards\n")
dealer_cards = dealer.shuffle()
human_score = [0]
computer_score = [0]
human_hand = players.take_first_cards()
computer_hand = players.take_first_cards()
computer_score_list = players.total_score(computer_hand, computer_score)
computer_score = sum(computer_score_list)          
human_score_list = players.total_score(human_hand, human_score)
human_score = sum(human_score_list)
display.display_hand(human_hand)
display.display_score(human_score)

def computer_logic(computer_score, computer_hand, computer_score_list):
# Computer Player Logic
    while computer_score < 22 and computer_score != 0:
    # The Dealer will always twist if score is 13 or under.
        if computer_score <= 13:
            computer_hand = players.twist(computer_hand)
            computer_score_list = players.total_score(computer_hand, computer_score_list)
            computer_score = computer_score + computer_score_list[-1]
            # The dealer will twist half the time if 13 < score < 17
        elif computer_score > 13 and computer_score < 17:
            random_number = random.randint(1, 2)
            if random_number == 1:
                computer_hand = players.twist(computer_hand)
                computer_score_list = players.total_score(computer_hand, computer_score_list)
                computer_score = computer_score + computer_score_list[-1]     
            else:
                # If over 17 the dealer will stick
                break         
        elif computer_score > 21:
            computer_score = 0
            return computer_score   
        else:
            return computer_score
    return computer_score    


# Human Controller
def human_player(human_score, human_hand, human_score_list, computer_score):
    while human_score < 22:
        user_choice = int(input("Do you want to Twist(1) or Stick(2)?: "))
        if human_score == 21 and computer_score != 21:
            print("You got 21!, Well done, you win!")
            break
        elif human_score > 21:
            print(f"Game Over, you are bust! Dealer had {display.display_hand(computer_hand)}")
            break
        elif user_choice == 1:
            human_hand = players.twist(human_hand)
            human_score_list = players.total_score(human_hand, human_score_list)
            human_score = human_score + human_score_list[-1]
            display.display_hand(human_hand)
            display.display_score(human_score)
        elif user_choice == 2:
            if computer_score > human_score:
                print(f"You lose! The dealer had: {computer_score}")
                break
            elif computer_score == human_score:
                print("It's a draw but dealer always wins")
                break
            else:
                print(f"You win! The dealer had: {computer_score}")
                break      
        else:
            print("Incorrect Input")
    return human_score
    


    
computer_score = computer_logic(computer_score, computer_hand, computer_score_list)
if computer_score > 21:
    computer_score = 0
human_score = human_player(human_score, human_hand, human_score_list, computer_score)
if human_score > 21:
    print("You bust, Game Over!")