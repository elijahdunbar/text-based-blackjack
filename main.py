############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from os import system, name
from art import logo

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def blackjack():
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  def show_hand(player, dealer):
    print(f"  Your cards: {player}, current score: {sum(player)}")
    print(f"  Computer's first card: {dealer[0]}")

  def deal(player, dealer, card_amt):
    while card_amt != 0:
      player.append(random.choice(cards))
      dealer.append(random.choice(cards))
      card_amt -= 1

    show_hand(player, dealer)

  def deal_to_player(player):
    player.append(random.choice(cards))

  def computer_draws(dealer):
    while sum(dealer) < 17:
      dealer.append(random.choice(cards))
      if sum(dealer) > 21:
        if 11 in dealer:
          dealer[dealer.index(11)] = 1
  
  keep_playing = True      
  
  def play_again():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
      clear()
      print(logo)
      blackjack()
    else:
      
      clear()

  player = []
  dealer = []
  
  deal(player, dealer, 2)
  while keep_playing:
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
      deal_to_player(player)
      if sum(player) > 21:
        if 11 in player:
          player[player.index(11)] = 1
          show_hand(player, dealer)
        else:
          print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nYou went over. You lose 😭")
          keep_playing = False
          play_again()
      elif sum(player) == 21:
        print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nYou got 21! You win 😁")
        keep_playing = False
        play_again()
      else:
        show_hand(player, dealer)
    else:
      computer_draws(dealer)
      if sum(dealer) > 21:
        print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nComputer went over. You win 😁")
        keep_playing = False
        play_again()
      elif sum(dealer) > sum(player):
        print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nComputer has a higher score. You lose 😭")
        keep_playing = False
        play_again()
      elif sum(dealer) == sum(player):
        print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nIt's a draw 😒")
        keep_playing = False
        play_again()
      else:
        print(f"    Your final hand: {player}, current score: {sum(player)}\n    Computer's final hand: {dealer}, final score: {sum(dealer)}\nYou have the higher score. You win 😁")
        keep_playing = False
        play_again()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  print(logo)
  blackjack()
