print('Welcome to my first game!')
player_name = input("What is your name? ")
print("Hey {name}!".format(name = player_name))
player_age = input("Before we get started, what is your age? ")

if int(player_age) > 12:
  print("Awesome! Since you are {age}, you are old enough to play!".format(age = player_age))
  ready = input("Are you ready to play?(yes or no?) ")
  if ready == "yes":
    print("Great! This is your first choice! You are on a random path and now have two ways to go.")
    first_choice = input("Left or Right ?")
    if 


else:
  print("Sorry! Since you are {age}, you are NOT old enough to play!".format(age = player_age))
  print("~~GAME OVER~~")