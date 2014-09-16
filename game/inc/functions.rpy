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


# def create_pablarales(game):
# Creates the pablarales character at the end of the game depending on gameplay vars
# return

# def final_report(game):
# Creates a final text report based on your decissions through the game
# return