# Act 2, Meet Compute

label a2_meetcompute_conversations:
    scene mal 00 with Dissolve(1)

    play music "audio/MeetCompute_TheChoice.mp3"

    "You are in the MIL, again on a late night."
    "This time you are digitizing Leisure Suit Larry for DOS (or Windows95?)."
    with hpunch
    show 0009 at center:
        zoom 1.9
    pause (0.35)
    hide 0009
    show macFront
    "You hear the sound and again the iMac is on."
    "You were sure it had not been earlier."
    "You had explicitly checked... {w}for some reason.{\w}"
    show macFront at macZoom
    pause (2)
    show textDisplay "Hi [_InputName]."
    $ renpy.pause(delay=None)
    show textDisplay "I was hoping you’d be back. I have a couple I want you to meet."
    $ renpy.pause(delay=None)
    "You don't believe your ears."
    with hpunch
    "But then, from behind you..."
    ti "Hi. Um. It’s Its. Its really nice to meet you."
    #zoom out from the mac here, slide it off screen, slide the ti on screen, then maybe pop in the odyssey from the side
    #mess with this later, for now, just getting things in place at least
    scene mal 01 with Dissolve(0.5)
    show ody45 at odyLeft
    show ti15 at tiRight
    "You whip around to see the monitor of the TI99 displaying spoken text."
    "You are speechless."
    #odyssey pops in
    ody "Yooooooo [_InputName]! This is so chill! I knew [_InputPronoun] would be a total chiller!"
    with hpunch
    hide ti15
    hide ody45
    show 0009 at center:
        zoom 1.9
    show ti15 at tiRight
    show ody45 at odyLeft
    pause(0.15)
    hide 0009
    pause (0.15)
    hide ti15
    hide ody45
    show 0009 at center:
        zoom 1.9
    show ti15 at tiRight
    show ody45 at odyLeft
    pause(0.35)
    hide 0009
    "The screen starts to go wavy." with hpunch
    "You are overwhelmed."
    with hpunch
    show 0009 at center:
        zoom 1.9
    pause(0.15)
    show 0001 at center:
        zoom 1.9
    pause (0.15)
    hide 001
    show 0009 at center:
        zoom 1.9
    pause(0.35)
    hide 0009
    scene black
    "You pass out." with hpunch
    scene mal 00 with Dissolve(2)
    "You regain consciousness."
    "From the floor, you hear the computers wondering if you're alright."
    ti "Oh Gosh! I hope [_InputPronoun] is ok!"
    ody "I bet [_InputName] is fine, bros. [_InputPronoun] is just excitable. You gotta stay chill!"
    #said shake text here, like hpunch or different?
    mac "[_InputName]! [_InputName]! {size=-7}Oh I learned about this! You have to raise [_InputPronoun] legs and {i}shake them{/i}!"
    mac "{size=+7}Help! Someone! Help {size=+5}Help {size=+5}Help!"
    "You get up, unsteadily."
    #[ a brief moment of wavy screen effect ] this should be better but im jsut overalaying ai for now
    show 0009 at center:
        zoom 1.9
    pause(0.35)
    hide 0009
    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft

    ### <MISSING TEXT> ###
    # WRITE: Each of the three computers say something that hints at their personality.

    "You are coming to terms that this is {i}not{/i} a game."
    "These computers have somehow become sentient."
    "You ask, confusedly: “What do I call you?”"
    all "I don't know..."
    all "Please tell me what you would like to call me."
    "Select which computer to name."
    menu:
        "iMac G3":
            jump name_Mac

        "TI-99":
            jump name_Ti

        "Magnavox Odyssey":
            jump name_ody
