import random

# Flags to track whether the player or dealer is still in the game
playerIn = True
dealerIn = True

# Initialize the deck of playing cards
deck = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', 
         '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', 
         '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', 
         '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']

# Initialize hands for player and dealer
playerHand = []
dealerHand = []

# Function to deal a card to a hand
def dealCard(turn):
    card = random.choice(deck)  # Select a random card from the deck
    turn.append(card)           # Add the selected card to the hand
    deck.remove(card)           # Remove the card from the deck

# Function to calculate the total score of a hand
def total(turn):
    total = 0
    # Define cards with numerical values
    numCards = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C']
    # Define face cards
    faceCards = ['JS', 'QS', 'KS',
                 'JH', 'QH', 'KH',
                 'JD', 'QD', 'KD',
                 'JC', 'QC', 'KC']
    aces = 0  # Counter for aces in the hand

    for card in turn:
        if card in numCards:
            total += int(card[:-1])  # Add the numerical value of the card
        elif card in faceCards:
            total += 10  # Face cards count as 10
        else:
            aces += 1  # Count the number of aces

    # Handle the value of aces (either 1 or 11)
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total

# Function to reveal the dealer's hand
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]  # Reveal only the first card if the dealer has two cards
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]  # Reveal first two cards if the dealer has more than two

# Main game loop
for _ in range(2):
    dealCard(dealerHand)  # Deal initial two cards to dealer
    dealCard(playerHand)  # Deal initial two cards to player

while playerIn or dealerIn:
    # Print the dealer's and player's hands
    if playerIn:
        print(f"Dealer has {revealDealerHand()} and X")
    else:
        print(f"Dealer has {dealerHand}")
    print(f"Player has {playerHand} score = {total(playerHand)}")
    
    # Player's turn to hit or stay
    if playerIn:
        playerChoice = input("1: Stay\n2: Hit\n")
        if playerChoice == '1':
            playerIn = False  # Player chooses to stay
        else:
            dealCard(playerHand)  # Player chooses to hit
    
    # Dealer's turn based on their score
    if total(dealerHand) > 16:
        dealerIn = False  # Dealer stays if score is over 16

    else:
        dealCard(dealerHand)
    
    if total(playerHand) >= 21 or total(dealerHand) >= 21:
        break

# Outcome and final reveal
if total(playerHand) == 21:
    print(f"Dealer's hand: {dealerHand} with a score of {total(dealerHand)}")
    print(f"Player's hand: {playerHand} makes Blackjack! Winner Winner Chicken Dinner!")
elif total(dealerHand) == 21:
    print(f"Dealer's hand: {dealerHand} makes Blackjack!")
    print(f"Player's hand: {playerHand} with a score of {total(playerHand)}. Dealer wins.")
elif total(playerHand) > 21:
    print(f"Dealer's hand: {dealerHand} with a score of {total(dealerHand)}")
    print(f"Player's hand: {playerHand} is over 21 and busts. Dealer wins.")
elif total(dealerHand) > 21:
    print(f"Dealer's hand: {dealerHand} is {total(dealerHand)} and busts.")
    print(f"Player's hand: {playerHand} with a score of {total(playerHand)}. You win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"Dealer's hand: {dealerHand} with a score of {total(dealerHand)}")
    print(f"Player's hand: {playerHand} with a score of {total(playerHand)}. Dealer wins.")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"Dealer's hand: {dealerHand} with a score of {total(dealerHand)}")
    print(f"Player's hand: {playerHand} with a score of {total(playerHand)}. You win!")
elif total(dealerHand) == total(playerHand):
    print(f"Dealer's hand: {dealerHand} with a score of {total(dealerHand)}")
    print(f"Player's hand: {playerHand} with a score of {total(playerHand)}. It's a push!")


