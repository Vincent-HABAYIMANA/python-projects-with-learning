import random

play = True
while  True:
 number_to_guess=random.randint(1,100)
#loop
 try:
   guess = int(input ('enter your guessing number between 1 and 100: '))
   if guess < number_to_guess:
     print ('Too low!')
   elif guess > number_to_guess:
      print('Too high!')
   else:
      print('Congratulation! you guessd the number.')
      break
 except ValueError:
    print('please enter a valid number')
    


