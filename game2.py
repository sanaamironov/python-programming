# File:  game.py
# Author:	Sanaa Mironov
# Date:	Oct 17,2017
# Section: 04
# Description:  Print list of games to user to vote on. Then 
#               prints the numbe of votes for each game. 
# Collaboration: During lab, collaboration between
# students is allowed, although I understand I still
# must understand the material and complete the
# assignment myself.

def main():
	GAME_SENTINEL = 0
	games = ["Twister", "Dodgeball", "Capture the Flag", "Hide and Seek", "Croquet", "Ring Toss", "Ping Pong"]

	for i in range(len(games)):
		print (i + 1 ,"-", games[i])
	
	votes = [0] * len(games)
	game_choice = int(input("What game would you like to play? (0 to quit): "))	
	
	while game_choice != GAME_SENTINEL:
		votes[game_choice - 1] = votes[game_choice - 1] + 1	
		game_choice = int(input("What game would you like to play? (0 to quit): "))	
		
	for i in range(0,len(votes)):
		print(games[i],"has",votes[i],"votes.")
main()		