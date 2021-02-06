print('Welcome to my first game!\n')
player_name = input("What is your name? ")
print("Hey {name}!\n".format(name = player_name.title()))
player_age = input("\nBefore we get started, what is your age? ")

if int(player_age) > 5:
  print("Awesome! Since you are {age}, you are old enough to play!".format(age = player_age))
  ready = input("\nAre you ready to play?(yes or no?) ")
  if ready == "yes":
    print("\nGreat! Here is your first choice! You are on a random path and now have two ways to go.")
    choice_1 = input("\nLeft or Right? ")
    #left side of path 
    if choice_1 == "left":
        print("\nYou travel down the left path and eventually you arrive at a brickhouse. This brickhouse has a dock with a boat attached to it to go accross the lake. Do you want to take the boat or go in the house?")
        choice_1 = input("\nboat or house? ")
        if choice_1 == "boat":
          print("\nYou jump inside the row boat that was tied to the dock. As you start to row the boat, you hear it creak as you slowly cross the lake. You start to get tired while rowing the boat while halfway on the lake. Do you want to stop or keep rowing?")
          choice_1 = input("\nstop or row? ")

        else:
          print("\nYou go to the front of the house and try to open the door. Apparently it is locked. Do you want to attempt to look for a key or kick the door in?")
          choice_2 = input("\nsearch or kick?")  
    #Right side of path     
    else:
      print("\nYou travel down the right path and you go deeper into a forest. Threes start to get denser and you start to lose your way. Eventually you arrive at an old shack. Do you want to enter the shack or try to find a way out of the woods?")
      choice_2 = input("\nshack or woods? ")
      if choice_2 == "shack":
        print()
        choice_1 = input()
      
      else:
        print()
        choice_2 = input()
  else:
    print("\nWhen you are ready just restart the game and be ready to play!")    


else:
  print("\nSorry! Since you are {age}, you are NOT old enough to play!".format(age = player_age))
  print("\n~~GAME OVER~~")