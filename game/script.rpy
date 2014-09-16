# Cryo Jelly - Chapter 00
# Define Characters and dialogues

define o = Character('Operator', color="#309d34")

# image dtime = Text(update(), xpos = 0.1, ypos = 0.1)

init: 
    $ time = 0
    $ timer_jump = 0


#Preliminar script
label start:
    #loop que se actualiza con tiempo
    # show dtime
    
    $time = 3600
    $timer_range = 1
    $timer_jump = 'end'
    show screen countdown


    "So you are determined..."
    "And completely sure that you want this..."
    "And I can't stop you"
    #"I understand that you are tired of the world"
    #"I understand that you are sick and sad"
    "So I just will assist you in the process"

    o "Welcome to your Cryo Jelly"
    o "This is the L-room"
    o "My name is Operator"
    o "We have 360 seconds to end this process."
    o "So please let's just start..."

# Clock function starts

# You have to take the initiative, there are some clues that indicate what you have to do or click

label end: 
    "You are over"

return

