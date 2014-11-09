# Cryo Jelly - Chapter 00
# Functions file

# Timer from: http://renpy.org/wiki/renpy/doc/cookbook/Timed_menus

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer .1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 2:
        text str(time) xpos .1 ypos .1 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xpos .1 ypos .1 at alpha_dissolve


# Live stats: they can be strings, floats, booleans...

screen quantum:
    text str("Quantum Phases/Nsec:") xpos .56 ypos.1 at alpha_dissolve
    $ random_number = renpy.random.randint(-3, 3)
    text str(random_number) xpos .91 ypos.1 at alpha_dissolve

screen thermal:
    text str("Thermal Kernel:") xpos .56 ypos.15 at alpha_dissolve
    $ random_number = renpy.random.randint(39982, 40008)
    text str(random_number) xpos .91 ypos.15 at alpha_dissolve
    
screen gluon:
    text str("Gluon Strong Interaction:") xpos .56 ypos.20 at alpha_dissolve
    $ random_number = renpy.random.randint(720, 723)
    text str(random_number) xpos .91 ypos.20 at alpha_dissolve
    
screen chromo:
    text str("Chromodynamics:") xpos .56 ypos.25 at alpha_dissolve
    $ random_number = renpy.random.randint(10000, 10002)
    text str(random_number) xpos .91 ypos.25 at alpha_dissolve

screen light:
    text str("Light Scattering:") xpos .56 ypos.30 at alpha_dissolve
    $ random_number = renpy.random.randint(5, 9)
    text str(random_number) xpos .91 ypos.30 at alpha_dissolve
    
screen opalescence:
    text str("Critical Opalescence:") xpos .56 ypos.35 at alpha_dissolve
    $ random_number = renpy.random.randint(99, 100)
    text str(random_number) xpos .91 ypos.35 at alpha_dissolve

screen quark:
    text str("Quark Confinment:") xpos .56 ypos.40 at alpha_dissolve
    $ random_number = renpy.random.randint(0, 1)
    text str(random_number) xpos .91 ypos.40 at alpha_dissolve


# def create_pablarales(game):
# Creates the pablarales character at the end of the game depending on gameplay vars
# return

# def final_report(game):
# Creates a final text report based on your decissions through the game
# return