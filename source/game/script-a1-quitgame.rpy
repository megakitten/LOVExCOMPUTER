# Act 1, Quit Game Branch

label quitGame:
    "You decide to turn off the computer instead."
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
    "You check the time and realize it's getting late. It's probably time to wrap up for the night."
    scene black
    "You shut the lights off and lock up the Media Innovation Lab. You're tired."

    return
