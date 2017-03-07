print('Welcome to the adventure story where your choose your path')

playerOne = raw_input('So player what is your name? ')

print('press enter to start the game')

doorOne = 1
doorTwo = 2
doorThree = 3


print('There are three doors that define your adventure. which door would your like to choose')
playerChoice =  int(raw_input(' For door one press 1, for door two press 2, for door three press 3 '))

if playerChoice  ==1 :
	print('There is no going back now lets start the adventure')
	print('press enter to continue')
	print('You just washed up on a beach in a unkown land. You see two chinese military men walking towards you.')
	playerChoice = int(raw_input("do you choose option 1 (type 1) which is to have the guards take you to a castle or option 2(type 2) which is you run away " ))
	if playerChoice == 1 :
		print(' you have now met an old man that reminds you of someone that you know from a long time ago.')
		x = raw_input('do you want to help(type help) him or leave(type leave)what do you choose?')

		if(x  == 'help'):
			print('Great choice')
			if(raw_input('Now that you have decided to help the old friend you need to wake him up from the dream you are in. (type wakeup) ') == 'wakeup'):
				if(raw_input('Now that you both have woken up from the deepest of dreams you can either risk your chance and fly(type fly) back to america or you can stay(type stay) in england for the rest of your life. which do you choose.') =='fly'):
					print(' CONGRATS you have finally made it home after your long journey and time away from your kids. Enjoy your life!')
				else:
					print('Bummer man you could have flown home and seen your kids. Try again.')
		elif(x == 'leave'):
			print('Oh boy the guards are running after you with weapons. It seems you made the wrong choice. ')
			if(raw_input('do you want to keep running(yes or no)') == 'yes'):
				print('Well shit you died')
				print(' Maybe you should play the game again and try to live')
			else:
				print('Too bad hot shot you got shot in the dome and you died')
				print( 'you should play again and try to make the right choice.')
	elif playerChoice == 2:
		print(' As you run away you see a boat and decided to drive away from the military men')
		if(raw_input( 'Do you want to keep driving off into the sunset and hope to find different land(yes or no)') == 'yes'):
			print(' well your boat blew up sorry about that try again')
		else:
			print('Well listen here hotshot if you think youre going to get to another part of land you are wrong. best of luck trying to survive. Oh and you died, try again')


elif playerChoice == 2 :
	print('There is no going back now lets start the adventure')
	print('press enter to continue')
	if(raw_input("well you choose the wrong door but do you wish to continue(type yes)")) == 'yes':
		print('Since you choose door two you get the special abality to fly back home. If you want to actually play the game try again')
elif playerChoice == 3:
	print('There is no going back now lets start the adventure')
	print('press enter to continue')
	if(raw_input(' oh boy you choose the door with your crazy wife. Do you wish to continue?(yes or no)') == 'yes'):
		print(" you walked into your honeymoon room and see that the room is destroyed and the window open")
		if(raw_input( 'would you like to see whats out the window(yes or no)') =='yes'):
			print(' Mol is out on the window sill and looks you in the eyes and starts to speak')
			print('Youre waiting for a train. A train that will take you far away. You know where you hope this train will take you, but you dont know for sure. But it doesnt matter, because we will be together.')
			if(raw_input("now that youve heard the poem do you wish to continue watching ") == 'yes'):
				print('welp she jumped off the roof and died try again')
			else:
				print("too bad shes dead now try again")


