# The game of memory or concentration written in Python.
import random
formatted_array = []

cards_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create deck as JSON object
def create_deck(deck):   
    for value in cards_values:
        for suit in cards_suits:
            if suit == 'Hearts' or suit == 'Diamonds':                
                card = {
                    'value': value,
                    'suit': suit,
                    'colour': 'Red'
                }
            else:
                card = {
                    'value': value,
                    'suit': suit,
                    'colour': 'Black'
                }
            deck.append(card)

    # Shuffle the deck
    random.shuffle(deck)
    return deck

# Select two cards at random
def select_cards(deck):
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    while card1 == card2:
        message = '*** Duplicate cards selected. Re-selecting... ***'
        formatted_array.append(message)        
        card1 = random.choice(deck)
        card2 = random.choice(deck)
    else:
        return card1, card2
#end select_cards

def select_card_with_memory(deck, remember):
    card1 = random.choice(deck)
    card2 = random.choice(deck)

    for (match1) in remember:
        if card1["value"] == match1["value"] and card1["colour"] == match1["colour"]:
            card2 = match1
            message = "!!! I remember this card !!!"
            formatted_array.append(message)
            break        

    while card1 == card2:
        message = '*** Duplicate cards selected. Re-selecting... ***'
        formatted_array.append(message)
        card1 = random.choice(deck)
        card2 = random.choice(deck)    
    
    remember.append(card1)
    remember.append(card2)
    
    return card1, card2
#end select_card_with_memory

def main():
    max_iterations = 663 #1326
    hits = 0
    misses = 0
    deck = []
    cards = []
    drawn = []
    writefile = False #True
    remember = []

    deck = create_deck(deck)

    for i in range(max_iterations):
        #cards = select_cards(deck)
        cards = select_card_with_memory(deck, remember)
        while cards in drawn:
            message = '### Pair already matched ###'
            formatted_array.append(message)
            #cards = select_cards(deck)
            cards = select_card_with_memory(deck, remember)
        
        if (cards[0]["value"] == cards[1]["value"]) and (cards[0]["colour"] == cards[1]["colour"]):
            hits += 1
            drawn.append(cards)
            message =f"+ {i+1}: {cards[0]["value"]} of {cards[0]["suit"]} and {cards[1]["value"]} of {cards[1]["suit"]}"
            formatted_array.append(message)
        else:
            misses += 1
            message =f"- {i+1}: {cards[0]["value"]} of {cards[0]["suit"]} and {cards[1]["value"]} of {cards[1]["suit"]}"
            formatted_array.append(message)

    formatted_array.append(f'\nAfter {max_iterations} iterations:')
    formatted_array.append(f'Total hits: {hits}')
    formatted_array.append(f'Total misses: {misses}')
    formatted_array.append(f'Hit ratio: {hits/max_iterations:.2%}')
    formatted_array.append(f'Miss ratio: {misses/max_iterations:.2%}')

    for items in formatted_array:
        print(items)

    if writefile:
        with open('memory_game.txt', 'a') as f:
            f.write('\n\n**********\n\n')
            for items in formatted_array:
                f.write("%s\n" % items)
        f.close()
#end main

if __name__ == '__main__':
    main()