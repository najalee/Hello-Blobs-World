# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters
define b = Character("Blob")
define n = Character("")
# define f = Character("Fill in the blank:")
default fillInBlank = ""
define m = Character("Mission Contraol")

# Scaling images
image happyBlob = im.Scale("/blob emotions/blob happy.png", 657, 464.5)
image manualBlob = im.Scale("/blob emotions/blob reading manual.png", 700, 486)
image deadBlob = im.Scale("/blob emotions/blob dead.png", 657, 464.5)
image existingBlob = im.Scale("/blob emotions/blob existing.png", 657, 464.5)

# Scaling scenes
image goingForward = im.Scale("Going forward a planet.png", 1920, 1080)
image rsHappy = im.Scale("/rocket ship/rocket ship happy.png", 1920, 1080)
image rsBored = im.Scale("/rocket ship/rocket ship bored.png", 1920, 1080)
image rsSad = im.Scale("/rocket ship/rocket ship sad.png", 1920, 1080)
image rsCrash = im.Scale("/rocket ship/rocket ship crash.png", 1920, 1080)
image fightI = im.Scale("/fight/fight initial encounter.png", 1920, 1080)
image fight = im.Scale("/fight/fight encounter.png", 1920, 1080)
image qWing = im.Scale("/discoveries/questioning wing finding.png", 1920, 1080)
image fWing = im.Scale("/discoveries/found wing.png", 1920, 1080)
image cTOS = im.Scale("/discoveries/convused top of the ship finding.png", 1920, 1080)
image fTOS = im.Scale("/discoveries/found top of the ship.png", 1920, 1080)
image qSM = im.Scale("/discoveries/questioning starmap finding.png", 1920, 1080)
image fSM = im.Scale("/discoveries/found starmap.png", 1920, 1080)
image toPlanetT = im.Scale("/transitioning between planets/Going back to planet.png", 1920, 1080)
image bgPOne = im.Scale("/backgrounds/bg planet1-1.png", 1920, 1080)
image space = im.Scale("/backgrounds/bg buffer.png", 1920, 1080)


# The game starts here.

label start:

    scene space
    show rsHappy
    pause 2.0

    hide rsHappy
    show rsBored
    pause 1

    hide rsBored
    show rsSad 
    pause 0.2

    hide rsSad
    show rsCrash
    pause 2


    n "Oh no! Brave Captain Blob has crash landed on Haley\’s Comet! He needs your help to get back home!"

    n "Mission: Collect the wing of Blob\’s spaceship!"

label blobManual:
    scene bgPOne

    show manualBlob:
        yalign 0.9
        xalign 0.5

    n "Blob needs to send a message! To write a message, use the print command like in this example: print(‘Hello World!’)"
    
    hide manualBlob
    show fightI

    n "Watch out! Blob has been surrounded, use what you learned to help him!"
    hide fightI

    show fight 
    n "What is the command to write a message?"
    menu: 
        "print":
            # correct
            scene bgPOne
            show happyBlob:
                yalign .9
                xalign .5
            n "Great job! You beat the monsters!"
        "write":
            scene bgPOne
            show deadBlob:
                yalign .5
                xalign .5
            n "Oh no Captain Blob! Quick, get back to the ship to recover and try again"
            jump blobManual
        "send":
            scene bgPOne
            show deadBlob:
                yalign .5
                xalign .5
            n "Oh no Captain Blob! Quick, get back to the ship to recover and try again"
            jump blobManual

    hide happyBlob
    show qWing:
        yalign .9
        xalign .5
    b "Huh? What's this?"
    hide qWing
    show fWing:
        yalign .9
        xalign .5
    pause 2
    b "We found it! The wing to my ship! Thank you for your help!"  
    hide fWing
    show happyBlob:
        yalign .9
        xalign .5
    pause 1
    
    hide happyBlob

    show existingBlob:
        yalign .7
        xalign .1
    n "We need to let Home Base know Blob is okay! Send them a message that says 'Captain Blob reporting in!' using the command you learned earlier!"
    $ fillInBlank = renpy.input("Send them a message that says “Captain Blob reporting in!” using the command you learned earlier!", length = 50)

    if fillInBlank == "print('Captain Blob reporting in!')":
        jump finalWorldOne
        
    else:
        n "That's not right, get back to the ship to recover and try again!"
        jump blobManual


label finalWorldOne:
    m "kshhs...This is mission control.. kshss... we recieved your message."
    m "..."
    m "... ..."
    m "... ... ..."
    m "We have located your Star Map on the nearest planet to you. We've sent details, over and out."

    label fixingShipWing:
    n "Blob has to reattach the wing to his ship. Help him attach it by using the print command to turn on the ship, saying 'Power on'"

    $ fillInBlank = renpy.input("Help him attach it by using the print command to turn on the ship, saying 'Power on'", length = 50)

    hide existingBlob
    if fillInBlank == "print('Power on')":
        show happyBlob
        n "Great! Now Blob can travel to the next planet!"
        
    else:
        n "That's not right, get back to the ship to recover and try again!"
        jump fixingShipWing


    hide happyBlob
    scene space
    show toPlanetT
    with dissolve 
    pause 200




# Quiz One:
# Mission control wants Blob to confirm he’s okay, so he has to send them a hello world  message!
# “We need to let Home Base know Blob is okay! Send them a message that says “Captain Blob reporting in!” using the command you learned earlier!” 
# Choose the correct code snippet for creating “Hello World”
# ___(“Captain Blob reporting in”)
# ________ - 
# compare to print(“Captain Blob reporting in!”) and
# print(‘Captain Blob reporting in!”)


#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg planet1

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show blob:
#         yalign 0.5
#         xalign 0.5

#     # These display lines of dialogue.

#     b "Am I cool?"
#     menu:
#         "yes":
#             b "ya ik"
#             jump scene2
#         "no":
#             b "i hate you"

#     b "This is the second text!"

#     b "Another one"

# label scene2:
#     scene goingForward
    

#     b "we're in a new spot bcuz im cool"
    

    # This ends the game.

    return
