#!/usr/bin/env python
# coding: utf-8

# # Nedap Technical Test

# __Snakes and Ladders__
# 
# increment position with a 6 sided dice throw
# 
# If any special event occurs, print what happens

# In[1]:


import random


# Dice Throw function that increments player position with a random number between 1 and 6

# In[2]:


def dice_throw(player_position):
    increment = random.randint(1,6)
    print("player threw a {}".format(increment))
    
    new_position = player_position + increment
    print("Current position is {}".format(new_position))
    return new_position


# Ladder function that checks whether the player goes up a ladder

# In[3]:


def ladder_func(player_position):
    if player_position == 3:
        player_position = 11
        print("Ladder brought you up to {}".format(player_position))
        return player_position
    elif player_position == 6:
        player_position = 17
        print("Ladder brought you up to {}".format(player_position))
        return player_position
    elif player_position == 9:
        player_position = 18
        print("Ladder brought you up to {}".format(player_position))
        return player_position
    elif player_position == 10:
        player_position = 12
        print("Ladder brought you up to {}".format(player_position))
        return player_position


# Snake Function checks whether a player should be bitten by a snake

# In[4]:


def snake_func(player_position):
    if player_position == 14:
        player_position = 4
        print("Snake brought you down to {}".format(player_position))
        return player_position
    elif player_position == 19:
        player_position = 8
        print("Snake brought you down to {}".format(player_position))
        return player_position
    elif player_position == 22:
        player_position = 20
        print("Snake brought you down to {}".format(player_position))
        return player_position
    elif player_position == 24:
        player_position = 16
        print("Snake brought you down to {}".format(player_position))
        return player_position


# The actual game Snakes and Ladders

# In[5]:


def Snakes_and_Ladders():
    
    key = input("Press Enter to throw the dice")
    
    position = dice_throw(1)
    
    while position < 25:


        if position in [3, 6, 9, 10]:
            print("You go up a ladder")
            position = ladder_func(position)
        elif position in [14, 19, 22, 24]:
            print("Snake bit you")
            position = snake_func(position)
        
        print("\n")
        
        key = input("Press Enter to throw the dice")
            
        position = dice_throw(position)
            
    print("You win, you made it past position 25!")


# In[6]:


Snakes_and_Ladders()


# In[ ]:




