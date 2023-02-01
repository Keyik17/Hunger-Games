#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:47:20 2022
The game is is not finished.
@author: keyik
"""
import sys
import time

a = 2
b = 0.5
backpack = ['cookie', 'map', 'torch', 'scissors']
pocket = ['wet map']
game_over = '''

    ****************** 
    *                * 
    *    GAME OVER   *  
    *                *  
    ******************

    THANKS FOR PLAYING!
'''
win = '''   **********************
            *                    *
            * CONGRATS! YOU WIN! *
            *                    *
            **********************

Words can take us far but feelings last forever. I hope I made you feel something, dear reader. Something beautiful…

...words that carried us so far to share a novel.")

'''

def intro():
    print("***************************************************************")
    print("                          INTRO                              ")
    intro = '''
    “Darling, promise you will find the letter. I love you."
'''
    intro1 = '''
YOU FIND YOURSELF IN A GARDEN FULL OF FLOWERS.
     '''
    intro2 = '''
THE WIND BLOWS UPON YOUR BODY ON A SWING
THAT SWINGS LIGHTLY AGAINST THE FORCE OF THE AIR.
'''
    intro3 = '''
THE SCENE IS MAGNIFICENT AND FREE. WONDERFUL AND LONESOME.
'''
    intro4 ='''
YOU HOLD THE MAP, YOUR GRANDMOTHER INHERITED, 
IN HOPES OF YOU FINDING THE TREASURE BOX.
'''
    intro5 = '''
    "Rest in peace grandma. No matter what, I will find the letter"
''' 
   
    print()
    print(intro)
    time.sleep(a)
    print(intro1)
    time.sleep(a)
    print(intro2)
    time.sleep(a)
    print(intro3)
    time.sleep(a)
    print(intro4)
    time.sleep(a)
    print(intro5)
    time.sleep(a)
    print()
    print("***************************************************************")
    intro6 = '''
 From here you have three routes to choose from:
'''
    routes = '''
    1. GO TO A MAZE. (I am sorry, please do not choose this option as the game is not modified)
    2. STAY IN THE GARDEN. (I am sorry, please do not choose this option as the game is not modified)
    3. VISIT THE OCEAN.
'''
    print(intro6)
    time.sleep(a)
    print(routes)
    time.sleep(a)
    first_route = input(" Where would you like to travel? (1/2/3): ")
    if first_route == "1":
        print()
        route1()
    elif first_route == "2": 
        print()
        route2()
    elif first_route == "3":
        print()
        route3()


def Main_route1():
    print()


def route1():
    print()

def route1_1():
    print()

def route1_2():
    print()


def Main_route2():
    final_message = '''
    My darling, I love you so much. 

    I hope today is one the days when you live as if there is no tomorrow. 
    Perhaps, there is no tomorrow for we live the same day over and over again?
    In life we often forget what is really important...
    connections we make, the stories we share.

    What is really important for you? 

    I hope you won't get caught up with life. 
    You feel the most alive when you are outside of people's affairs, course of actions, responsibilities laid upon you.
    Maybe that is why we are lost?
    Zoom out and expand your horizons. 
    I promise you, no matter where you are in life, you are doing great. 
    Be open, free and whole regardless. 

    And if you ever set your mind to something, 
    remember...
    ...whoever travels without clarity, will need years for a one-day journey. 

    To live is a personal work of art. How sad...It only takes a life to learn how to live. 
    I love you my dear. I might not be able to look at your eyes and fill your heart with love. 
    But the message is immortalised in the letter. Come back and make your heart full of love and soul free of struggles. 

    Be whole regardless.
                    - with love Grandma.
    '''
    print("'I melted down crying, how can I not when all I yearn for is to listen to your novels?'")
    time.sleep(b)
    print("'I put down my heavy box and reach my arms with slight relief to hold yours.'")
    print("'To peek at what loveliness relies deep down on, what memories you carry, and what mysteries you hold.'")
    print("'I empty my hands to reach out for yours, grandma.'")
    time.sleep(b)
    print("'I take a look and see myself in the reflection of a deep ocean.'")
    print("'But there is so much more beyond the horizons of blue-infinity.'")
    print()
    print("'Terrific yet mesmerizing. Creatures and mysteries, everlasting fantasy, slow motion of the water.'")
    print()
    print("'A fascinating world indeed...your treasure box.'")
    time.sleep(b)
    print("'And in the end, I take something beloved with me.'")
    print("'You grant a piece of item. A valuable treasure I put into my box.'") 
    print()
    print("'So when I uncover mine, I display with great honor.'")
    time.sleep(b)
    print(win)
    exit()

def route2():
    print("Not too far from the shore, there is a cottage.")
    print()
    print("‘Why not go inside?’")
    print()
    print("The cottage seems to be on the map.")
    print("Carefully, once you approach the building, your eyes are caught on a beautiful tree outside of the cottage.")
    time.sleep(b)
    print("You go inside and observe the room. ")
    print("There is a huge couch with a wooden table in front of it.")
    time.sleep(b)
    options_route2 = '''
    1. MAKE SOME TEA AND ENJOY THE AESTHETICS.
    2. GO OUTSIDE TO OBSERVE THE TREE.
    '''
    print(options_route2)
    decision_route2 = input('Please choose (1/2): ')
    if decision_route2 == "1":
        print("The tea your grandmother used to make, reminds you of her.")
        print("Not even a single day goes by, without you recalling the memories of your grandmother.")
        time.sleep(b)
        print("Now you are feeling sad and decide to rest on a couch.")
        print()
        print("You fall asleep...slowly drifting away, you doze off.")
        print()
        time.sleep(b)
        print("The day goes by...")
        print("...another day without accomplishing your goal.")
        time.sleep(b)
        print()
        print("‘Grandma, I will search for the treasure tomorrow I guess...’")
        time.sleep(b)
        print(game_over)
        exit()

    else:
        print("The tree is so magnificent, full of flowers, lightly falling down.")
        time.sleep(b)
        print("The significance of the tree makes you look tiny in the face of the world.")
        time.sleep(b)
        print("As if it’s the nature looking upon us.")
        print()
        print("You pull up the map.")
        print()
        print("‘This tree looks exactly like on the map!’")
        print()
        print("You get closer and a notice a tiny box at the very corner of the giant tree.")
        print()
        time.sleep(b)
        print("‘There is a hole on a box.’")
        print()
        time.sleep(b)
        print("IMPORTANT: MAYBE YOU WILL WANT TO VIEW YOUR BACKPACK FOR THE ITEM TO OPEN THE BOX?")
        print()
        time.sleep(b)
        final_option = input('Please make a decision (Yes/No): ')
        if final_option == "YES" or final_option == "yes" or final_option == "Yes":
            print(backpack)
            my_item = input("What item do you need?: ")
            if my_item in backpack:
                backpack.remove(my_item)
                print(backpack)
                Main_route2()
        else:
            print("I am afraid you do not obtain the necessary item to open the box. ")
            print("...you were so close to finding what is in inside of the box...")
            
            time.sleep(b)
            print(game_over)
            exit()

def route2_1():
    print(" The cookie was nice’ - you tell yourself")
    time.sleep(b)
    print(" Surprisingly, you do not feel too hungry, rather energised to to continue!")
    time.sleep(b)
    print(" You make a move, and see multiple shells around the shore.")
    time.sleep(b)
    print(" And something shiny, right underneath one of them.")
    print(" You get closer and see...")
    print()
    time.sleep(b)
    print("‘Oh. It’s a key!’")
    key_decision2 = '''
    1. PICK UP THE KEY.
    2. DON'T TOUCH. 
    '''
    print(key_decision2)
    decision2 = input(" what is your choice? (1/2): ")
    if decision2 == "1":
        backpack.append('key')
        print("You have a new item in you backpack!")
        print(backpack)
        route2()
    else:
        print("I hope you will not regret your decision.")
        route2()


def route2_2():
    print("The water is warm. It surrounds your feet and brings the memories back.")
    print("You are enjoying the walk until you realise it is almost dawn.")
    time.sleep(b)
    print("You pull up the cookie from your backpack and decide it is a great time for dinner.")
    time.sleep(b)
    options_for_route2 = ''' 
    1. DO YOU THINK YOU SHOULD EAT THE COOKIE AND CONTINUE THE JOURNEY? 
    2. GO BACK, COOK THE MEAL, AND MAYBE EVEN INVITTE YOUR FRIENDS OVER FOR THE DINNER?
    '''
    print(options_for_route2)
    second_route2 = input("Please choose one of the options (1/2): ")
    time.sleep(b)
    if second_route2 == "1":
        route2_1()
    else:
        print(" So, you decide to have a proper meal for dinner. Good choice!")
        print(" You go back to your mansion and pass the beautiful garden.")
        print()
        print(" ...’One of the world’s beauties’ - you think.")
        print()
        print(" The sky looks exceptionally beautiful today.")
        print(" Today’s meal is turkey with lots of pastries for desert. Your guests liked the food.")
        print(" Now you feel tired and have no energy to continue this journey and decide to go back to sleep.")
        print(" You look at your calendar….it’s been 3 months since your grandmother passed away.")
        print()
        print("'I will continue the journey tomorrow.’ - you say to yourself....yet never arriving to your final destination.")
        time.sleep(b)
        print(game_over)
        exit()

def Main_route3():
    print()

def route3():
    print(" So you decide to visit the ocean.")
    print(" Your grandmother loved taking you swimming.")
    print(" The waves remind you of the carefree summer.")
    print(" As you get closer to the shore, you feel the urge to", end='')
    print(" go into the ocean and sense the depths of the water. ")
    time.sleep(b)
    print()
    choices = '''
    1. GO INTO THE OCEAN. 
    2. WALK AROUND THE SHORE.
    3. COLLECT THE SHELLS. (Please do not choose this option)
    4. FEED THE SEAGULL WITH A CHOCOLATE CHIP COOKIE. (Please do not choose this option)
'''
    print(choices)
    second_route = input(" What will your choice be? (1/2/3/4/5): ")
    if second_route == "2":
        route2_2()
    elif second_route == "3":
        route1_1()
    elif second_route == "4":
        route1()
    else:
        print()
    
    print(" Slowly going into the turquoise shallow, ", end='')
    print("the choppy waves gently touch your skin.")
    time.sleep(b)
    print(" You see the ethereal light in azure water, illuminating the sun")
    print(" Peace hypnotically surrounds you,", end='')
    print(" letting you forget about the letter")
    time.sleep(b)
    print(" Serene, whispering in your ear, for you get distant from the shore.")
    print()
    time.sleep(b)
    options = '''
    1. TOSS AWAY THE SHOES AND THE BACKPACK AND KEEP YOUR HEAD UP.
    2. ALLOW THE WATERS TO WEIGH YOU DOWN.
'''
    print(options)
    print()
    time.sleep(b)
    third_route = input("PLeasse select (1/2): ")
    if third_route == "1":
        route3_1()
    elif third_route == "2":
        route3_2() 
        
def route3_1():
    print()
    print(" As you start breathing steadily, you find yourself swimming back to the shore.") 
    time.sleep(b)
    print(" Barely survived, you lost all your belongings in the ocean including your backpack. ")
    time.sleep(b)
    print(" The only thing remaining is the map that was left by your grandmother , ", end='')
    print("all wet and clenched in your hands.")
    time.sleep(b)
    print()
    print(' "Phew, that was close. I need to get out of here"')
    print()
    print(" Once you move your leg, you stumble upon somtheing shiny")
    print()
    print(' "Is it a key?" ')
    time.sleep(b)
    key_decision = '''
    1. TAKE IT.
    2. LEAVE IT.
'''
    print(key_decision)
    time.sleep(b)
    decision = input("Please choose (1/2): ")
    if decision == "1":
        pocket.append('key')
        print(" Now you have one more item in your pocket.")
        print(pocket)
        route2()
    else:
        print(" Hope you will not regret the choice.")
    Main_route3()

def route3_2():
    print()
    print(" At this point you cannot swim anymore.")
    time.sleep(b)
    print(" As you get unconscious, far away from space and time, ", end='')
    print("sinking deep into the water...")
    time.sleep(b)
    print(" ...you say your last words...")
    print()
    time.sleep(b)
    print(' "Grandma, I am sorry. I guess I am coming to you." ')
    print()
    time.sleep(b)
    print(game_over)
    exit()

print()
print("     ******************  ")
print("     *                *  ")
print("     *    WELCOME     *  ")
print("     *                *  ")
print("     ******************  ")
print()
time.sleep(b)
name = ' '
def the_beginning():
    start = input(" Are you ready for the adventure?(Yes/No): ")
    if start == "Yes" or start == "yes":
        name = input(" Please enter your name: ")
        intro()
    elif start == "No" or start == "no":
        print()
        print(" Maybe next time. Hope to see you soon!")
        print()
    else:
        print("Please try again. You might have mistyped :) ")
        the_beginning()
    start = start.split()
the_beginning()


    


