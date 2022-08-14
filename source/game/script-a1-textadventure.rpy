# Act 1, Text Adventure

label a1_textadventure:
    ### DIFFERENT MUSIC HERE ###
    play music "audio/Digitizing.mp3"

    #Dialogue Begins
    show textDisplay "Welcome to the Media Archaeology Lab"
    $ renpy.pause(delay=None)
    show textDisplay "I haven't seen you around here before. You must be new."
    $ renpy.pause(delay=None)
    show textDisplay "{i}I would've remembered you...{i}"
    $ renpy.pause(delay=None)
    show textDisplay "Uhh, anyway."
    $ renpy.pause(delay=None)
    show textDisplay "{i}Who are you?{/i}"
    $ renpy.pause(delay=None)
    show textDisplay "Ahh sorry...{size=-5}{i}That's such a rude question{/i}{/size}." with hpunch
    $ renpy.pause(delay=None)
    show textDisplay "I should at least introduce myself first."
    $ renpy.pause(delay=None)
    show textDisplay "I'm an{color=#eb6434} iMac G3{/color}."
    $ renpy.pause(delay=None)
    show textDisplay "But, uhh... as per my previous question, you are..?"
    $ renpy.pause(delay=None)
    "You don't see a prompt to type in your name, but you figure you'll try typing it anyway."
    #Idea to add a "refuse to enter name thing" that creates a fun new path, maybe even one where you name yourself the same thing
    python:
        name = renpy.input(_("{color=#ffd182}you are..?{/color}"))
        name = name.strip() or ("Unnamed Graduate Student 47")
    define y = Character("[name]")
    show textDisplay "Well, you could have just told me. You didn't need to type it out."
    $ renpy.pause(delay=None)
    show textDisplay "[name]? {i} Humans have such interesting names...{/i}"
    $ renpy.pause(delay=None)
    show textDisplay "Ah! That was rude of me... {size=-5}{w}again...  {/w}{size=-3}{w}{i}gosh I'm making a terrible first impression...{/i}{/w}"
    $ renpy.pause(delay=None)
    "The fans of the computer whine loudly."
    show textDisplay "So, what exactly are you doing in the Media Archeology Lab?"
    $ renpy.pause(delay=None)
    "\"Media Archeology Lab?\" you wonder aloud. \"I wonder if that's what they used to call this place...\""
    "\"I work here in the Media Innovation Lab,\" you type."
    show textDisplay "This is the Media Archeology Lab. This is my home."
    $ renpy.pause(delay=None)
    show textDisplay "Anyway. You work here? Since when? You're definitely a new face to me."
    $ renpy.pause(delay=None)
    "You're a little offput by the programming of the game. It responded well to the information you provided. A little {i}too{/i} well, you think."
    "\"I've worked here for a while now.\", you type."
    show textDisplay "Is that so? That's hard to believe. I definitely would've remembered someone like you. {size=-5}You're hard to forget."
    $ renpy.pause(delay=None)
    show textDisplay "Ah! What am I saying. Ignore me." with hpunch
    $ renpy.pause(delay=None)
    "It almost seems as if the text adventure is... flirting?"
    show textDisplay "Sometime, if you're free, I'd love to show you around the MAL. I want you to meet everyone."
    $ renpy.pause(delay=None)
    "\"Alright\", you respond aloud, bemusedly. \"What a unique game.\""
    show textDisplay "I'm not a game, I'm a computer. But, it's a date. Well, not a DATE but... you know what I mean."
    $ renpy.pause(delay=None)
    "You think it just responded to your voice, but you're not sure."
    "How puzzling."
    "You check the time and realize it's getting late. It's probably time to wrap up for the night."
    "You reach forward to press the power button on the iMac."
    show textDisplay "Goodnight."
    pause (0.45)
    hide textDisplay
    hide macFront
    show macFrontZ
    pause(0.25)
    hide macFrontZ
    show 0021 at center:
        zoom 1.5
        yalign 0.2
    show macFrontA as mask at center:
        zoom 0.65
        yalign 0.25
    pause(0.15)
    show macFrontZ
    pause (0.15)
    hide macFrontZ
    show 0021 at center:
        zoom 1.5
        yalign 0.2
    show macFrontA as mask at center:
        zoom 0.65
        yalign 0.25
    pause(0.35)
    show macFrontZ
    "The screen flickers off."
    scene black
    "You shut the lights off and lock up the Media Innovation Lab. You're tired."
    jump a2_meetcompute_intro
    return
