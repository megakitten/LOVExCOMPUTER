# The script of the game goes in this file.

define mac = Character(
"iMac G3",
who_color="#eb6434", who_font="ChicagoFLF.ttf", who_size=40,
what_color="#ffd182", what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

define ti = Character(
"TI-99",
who_font="ChicagoFLF.ttf", who_size=40,
what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)

define ody = Character(
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

image ody45:
    "Odyssey 04.png"
    zoom 0.25
    yalign 0.5

transform odyLeft:
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
default _OdyName = "Magnavox Odyssey"
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
            jump startGame

        "No":
            jump quitGame

label start:

    jump a1_textadventure

    return
