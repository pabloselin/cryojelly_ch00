# Cryo Jelly - Chapter 00
# Define Characters and dialogues

#Operator
define o = Character('Operator', color="#309d34")
define t = Character ('Tester', color="#bf0000")

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
    
    # On screen stats
    show screen quantum
    show screen thermal
    show screen gluon
    show screen chromo
    show screen light
    show screen opalescence
    show screen quark

    "So you are determined..."
    "And completely sure that you want this..."
    "And I can't stop you"
    "So I just will assist you in the process"

    o "Welcome to your Cryo Jelly"
    o "This is the L-room"
    o "My name is Operator"
    o "We have 360 seconds to end this process."
    o "So please let's just start..."

    "CRYO JELLY: Cryogenic - Quark Gluon Plasmatic Gelatin Solution."

    o "One envelope is enough to keep an average human inside a unit for a period of three years"
    o "Just fill a cubic container with destilated warm water, pour the contents of the envelope and wait for the particles to start interacting"
    o "It's a powdered particle accelerator, mixed with sacred herbs from the Andes mountains."
    o "When the solution starts to make bubbles you have to put the diodes (supplied with the Jelly Kit) into both extremes of the container ..."
    o "... the diodes will solidify instantly in that position and start the process that allows the human entity to merge with the solution"
    o "Once you feel ready (no more than 20 minutes after the diodes insertion) you have to submerge your body into the jelly."
    o "It is recommended to lay facing to the floor in order to avoid a nightmare stage that usually happens to the begginers."
    o "Once submerged you will start losing some of the limits of your awareness giving place for the MAI (Melted A. I.) to take the essential functions of your personality"
    o "A test will start soon and will give you the final indications. Thanks for reading."

    t "Hello asshole"
    t "I am the tester"
    # Las respuestas se almacenan y dan forma a pablarales al final
    t "Question Nº1:"
    t "You see a turtle upside down. Do you want to eat the turtle?"
    t "Question Nº2:"
    t "Boiling is to happiness as Melting is to?"
    # Algunas preguntas son de cálculo y miden el tiempo de respuesta (sería bueno que fueran cálculos variables para que nadie se lo pudiera aprender de memoria)
    t "Question Nº3:"
    t "Multiply 4x6.3"


# Clock function starts

# You have to take the initiative, there are some clues that indicate what you have to do or click

label end: 
    "You are over"

return

