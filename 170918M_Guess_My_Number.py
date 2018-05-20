import random
counter = 0
guess = int(input("1 - 100 guess a number. go "))
correct = random.randint(1, 100)


while guess != correct:
  guess = int(input())

  if(guess > correct):
  	  print('too high')
  elif( guess < correct):
   	  print('too low')
  else:
  	  print('there we go!')