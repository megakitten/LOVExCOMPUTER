# The script of the game goes in this file.

define mac = Character(
"iMac G3",
who_color="#eb6434", who_font="ChicagoFLF.ttf", who_size=40,
what_color="#ffd182", what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

define ti = Character(
"TI-99",
who_font="ChicagoFLF.ttf", who_size=40,
what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

define mo = Character(
"Magnavox Odyssey",
who_font="ChicagoFLF.ttf", who_size=40,
what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

define narrator = Character(
what_italic=True)

define all = Character(
"All",
who_font="ChicagoFLF.ttf", who_size=40,
what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

image macFront:
    "iMac 00.png"
    zoom 0.25
    yalign 0.1

image alphaset:
    "iMac 00 A 0.png"
    zoom 0.25
    yalign 0.1

image macFrontA = AlphaMask("iMac 00.png", "iMac 00 A 2.png")

image macFrontZ:
    "iMac 00.png"
    zoom 0.65
    yalign 0.25

transform macZoom:
    parallel:
        zoom 1.0
        linear 2.0 zoom 2.6

    parallel:
        yalign 0.1
        linear 1.0 yalign 0.25

transform macTop:
    zoom 0.8
    yalign 0.0
    xalign 0.5

image ti15:
    "TI99 01.png"
    zoom 0.25
    yalign 0.5

transform tiRight:
    xalign 0.8
    yalign 0.6

transform tiSpot:
    zoom 1.15
    xalign 0.5

image mo45:
    "Odyssey 04.png"
    zoom 0.25
    yalign 0.5

transform moLeft:
    xalign -0.2

image mal 00:
    "mal 00.jpg"
    zoom 1.6
    yalign 0.4
    rotate -3

image mal 01:
    "mal 01.jpg"
    zoom 1.5
    yalign 0.4

default _InputName = "Unnamed Graduate Student 47"
default _InputPronoun = "they"
default _MacName = "iMac G3"
default _TiName = "TI-99"
default _MoName = "Magnavox Odyssey"
image my_movie = Movie(channel="movie_dp", play="griddigitaldreaminsidebloodywires3.mp4")

image textDisplay = ParameterizedText(yanchor=920, xanchor=550, xysize=(1080,1080), font="ChicagoFLF.ttf", size=40, slow_cps=20)
#image textDisplay = ParameterizedText(yanchor=880, xanchor=220, xysize=(450,400), font="ChicagoFLF.ttf", size=20, slow_cps=20)

# The game starts here.

label start:

    scene mal 00 with Dissolve(1)

    # Narration
    "You are the newly hired graduate student tasked with digitizing the aging collection of the Media Innovation Lab at your university."
    scene mal 01 with Dissolve(0.5)
    "One late night, you are digitizing the game, \"Leather Goddess of Phobos\" made for the Apple II when you hear a noise behind you."
    with hpunch
    "A computer fan spins up to speed."
    scene mal 00 with Dissolve(0.5)
    "You look around, eventually tracing the sound to the iMac G3 in the corner of the lab."
    show macFront
    pause(0.25)
    hide macFront
    show 0021 at center:
        zoom 0.5
        yalign 0.2
    show macFrontA as mask at center:
        zoom 0.25
        yalign 0.1
    pause(0.15)
    show macFront
    pause (0.15)
    hide macFront
    show 0021 at center:
        zoom 0.5
        yalign 0.2
    show macFrontA as mask at center:
        zoom 0.25
        yalign 0.1
    pause(0.35)
    show macFront
    "As you approach, the screen flickers to life, accompanied by that characteristic whine of cathode ray tubes and static electricity."
    show macFront at macZoom
    "You approach the computer. A text box appears on the screen."
    show textDisplay "Welcome to the Media Archaeology Lab"
    "It says, \“Welcome to the Media Archaeology Lab\”"
    "\"Strange!\" you think to yourself."
    "One of the other student researchers must have been working on a text adventure."
    "Would you like to play it?"
    menu:
        "Yes":
            jump playGame

        "No":
            jump quitGame

label playGame:

    play music "audio/Digitizing.mp3"

    #Dialogue Begins
    show textDisplay "Welcome to the Media Archaeology Lab"
    $ renpy.pause(delay=None)
    show textDisplay "You must be new. I haven't seen you around here before."
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
    show textDisplay "I'm the{color=#eb6434} iMac G3{/color}."
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
    jump act1Introduction
    return
