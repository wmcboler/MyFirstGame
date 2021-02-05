print('Welcome to my first game!\n')
player_name = input("What is your name? ")
print("Hey {name}!\n".format(name = player_name.title()))
player_age = input("Before we get started, what is your age? ")

if int(player_age) > 12:
  print("Awesome! Since you are {age}, you are old enough to play!\n".format(age = player_age))
  ready = input("Are you ready to play?(yes or no?) ")
  if ready == "yes":
    print("Great! Here is your first choice! You are on a random path and now have two ways to go.\n")
    choice_1 = input("Left or Right ? ")
    if choice_1 == "left":
        print("\nYou travel down the left path and eventually you arrive at a brickhouse. This brickhouse has a dock with a boat attached to it to go accross the lake. Do you want to take the boat or go in the house?\n")
        choice_1 = input("boat or house? ")
        if choice_1 == "boat":
          print()
          choice_1 = input()

        else:
          print()
          choice_2 = input()  
        
    else:
      print("\nYou travel down the right path and you go deeper into a forest. Threes start to get denser and you start to lose your way. Eventually you arrive at an old shack. Do you want to enter the shack or try to find a way out of the woods?\n")
      choice_2 = input("shack or woods? ")
      if choice_2 == "shack":
        print()
        choice_1 = input()
      
      else:
        print()
        choice_2 = input()
  else:
    print("When you are ready just restart the game and be ready to play!")    


else:
  print("Sorry! Since you are {age}, you are NOT old enough to play!".format(age = player_age))
  print("~~GAME OVER~~")