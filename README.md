# Acey Deucey Calculator
_A Python program that calculates the probability of flipping a card between two others._


## What is Acey Deucey?
Acey Deucey, also known as Yablon, In-Between, Sheets, Between the Sheets or Maverick, is a simple betting card game. Two cards are dealt to a player, who then bets on whether the rank of a third card will fall between those of the first two. See https://en.wikipedia.org/wiki/Acey_Deucey_(card_game) for the rules of play.

## How to run
The program can be used strait from the command line or can be moved to a TI-nspire&trade; CX II calculator with python installed for a more portable version.

## Use
As the dealer flips the first two cards, enter the cards respective characters (_see below_). If the first two cards can not have any values between them (_e.i. King/King, 4/5_) then the program will move on to the next round. If there is, however, a possibility of flipping a card between the first two cards the program will output the probability in a percentage of that happening. Once the final card is revealed enter the value of that card as well so the program can _"Count Cards"_. You should also enter the cards dealt to other players if there are any.

## Character functions
| Character | Function |
| - | - |
| 2 to 9 | Cards from 2 to 9 |
| 1 | 10 card |
| j | Jack card |
| q | Queen card |
| k | King card |
| a | Ace card |
| x | Exit |

## Example Game
```
\Acey Deucey>python main.py
Round 1
>>> 29
48.0%
>>> k
Round 2
>>> 1a
23.4%
>>> 3
Round 3
>>> 45
No chance
Round 4
>>> 2a
90.5%
> 8
Round 5
> x
```
