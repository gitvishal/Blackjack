# !/usr/bin/python
import random
import sys

level = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
suits =  ['spade','heart','diamond','club']
points = [11,10,10,10,10,9,8,7,6,5,4,3,2]
cards = [(level[y],suits[x],points[y]) for x in range(4) for y in range(13)] #(level,suits,points)
random.shuffle(cards)

while 1 :
	try:
		wage_input = int(input('Enter the wage amount: '))
		break
	except :print 'Enter valid amount'

print "Dealing with cards ...."
user_cards = [cards.pop(),cards.pop()]
user_count = 0
dealers_cards=[cards.pop()]
dealers_count = 0
soft_hand = False
fold = False
winning_amount = 0
burst = False

for x in range(2):
	if user_cards[x][0] == 'A':soft_hand =True	
	user_count+=user_cards[x][2]

while True:
	print 'Enter choice'
	print '\n1: Hit \n2: Stand \n3: Fold'
	print '\ndealers cards : %s-%s' % (dealers_cards[0][0],dealers_cards[0][1])
	print 'dealers count: ',dealers_cards[0][2]
	print '\nplayers cards :'
	for x in user_cards:print '%s-%s' % (x[0],x[1])	
	print 'user count: ',user_count
	print '\n'

	try:
		choice = int(input('Enter the choice: '))
	except:
		print "Enter valid choice"
		choice = -1	
	if choice == 1:
		if soft_hand :
			soft_hand = False	
			for x in range(2):
				if user_cards[x][0] == 'A':
					user_count -= 10
					break
		user_cards.append(cards.pop())
		user_count += user_cards[-1][2]
		if user_count > 21:
			burst = True
			print 'burst','game over'
			sys.exit()
	elif choice == 2:
		if soft_hand :
			soft_hand = False	
			for x in range(2):
				if user_cards[x][0] == 'A':
					user_count -= 10
					break
		break
	elif choice == 3:
		print 'you have chooce to fold'
		winning_amount = .5 * wage_input
		print 'winning amount :',winning_amount
		sys.exit()
	else :print 'Enter valid choice'		

if not burst :		
	dealers_cards.append(cards.pop())
	for x in dealers_cards:dealers_count += x[2]
	while dealers_count < 17 :
		dealers_cards.append(cards.pop())
		dealers_count += dealers_cards[-1][2]
	print 'dealers point: %d \nplayers point: %d ' % (dealers_count,user_count)
	if dealers_count > 21 :
		print '\n\ndealer burst so player wins'
		print 'winning amount :', 2 * wage_input
		sys.exit()
	if user_count == dealers_count :print 'its a push'
	elif user_count > dealers_count :
		print '\n\nplayer wins'
		winning_amount = 2 * wage_input
		if user_count == 21 :
			print 'you got a blackjack'
			winning_amount += .5 * wage_input
		print 'winning amount :',winning_amount
	else :print '\n\nplayer loose. End game'