# Act 2, Meet Compute

label a2_meetcompute_conversation:
    scene mal 00 with Dissolve(1)
    play music "audio/MeetCompute.mp3"
    "...*unlock sfx*..."
    "You greets the familiar basement smell."
    "Another late night in the MIL."
    "You hope campus parking enforcement doesn't write you a ticket..."
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

    ### " Hello Hi Hello "
    voice "audio/Mac_line1.wav"


    show textDisplay "Hi [_InputName]."
    $ renpy.pause(delay=None)
    show textDisplay "I was hoping you’d be back. I have a couple I want you to meet."
    $ renpy.pause(delay=None)

    ### " I was hoping you’d be back. I have a couple I want you to meet. "
    voice "audio/Mac_line2.wav"

    "You don't believe your ears."
    with hpunch

    ### " Hi. Um. It’s Its. Its really nice to meet you. "
    voice "audio/TI_line6.wav"

    ### "Hi. Um. It’s Its. Its really nice to meet you."
    voice "audio/TI_line6.wav"

    "But then, from behind you..."
    ti "Hi. Um. It’s Its. Its really nice to meet you."
    ### TRANSITION

    #zoom out from the mac here, slide it off screen, slide the ti on screen, then maybe pop in the odyssey from the side
    #mess with this later, for now, just getting things in place at least


    scene mal 01 with Dissolve(0.5)
    pause(0.15)
    show ti15 at tiRight
    pause(0.15)
    show ody45 at odyLeft

    "You whip around to see the monitor of the TI99 displaying the words you just heard."

    ### ADD SCREEN SHAKE

    "~**WHAT**~ !!! ThE __=_) FvvvvvvvvC@#$!"

    #odyssey pops in

    ### " Yo I Mack! This is so chill! I knew this person would be totally chill!"
    voice "audio/Odyssey_line2.wav"

    ody "Yooooooo iMac!!! This is so chillllll!! I knew [_InputName] would be totally chill!" #[_InputPronoun]
    with hpunch
    "Hold it together!"
    pause(0.15)
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
    "You are oveRwHLPED!"
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
    "This is what passing out must be like..." with hpunch
    pause(0.15)
    scene mal 00 with Dissolve(2)
    "You regain consciousness."
    "From the floor, you hear the computers wondering if you're alright."

    ### " Oh Gosh! I hope it is ok! "
    voice "audio/TI_line7.wav"

    ti "Oh Gosh! I hope it is ok!"

    ### "Its fine! Just too excitable! I thought I said to stay chill!"
    voice "audio/Odyssey_line3.wav"
    ody "I bet [_InputName] is fine! [_InputPronoun] is just excitable. I thought I said to stay chill!"


    ### " Oh My God! I just learned this! You have to raise the legs and shake them! "
    voice "audio/Mac_line3.wav"

    mac "[_InputName]! [_InputName]! {size=-3}Oh {/size}I just learned about this! You have to raise [_InputPronoun] legs and {i}shake them{/i}!"

    ### " Oh no! How Do I shake someone's legs? "
    voice "audio/Mac_Line4.wav"

    mac "{size=+7}Oh NO! {/size}{size=+5}How Do *I* SHAKE{/size} {size=+7}[_InputPronoun] LEGS!{/size}"
    pause(0.55)
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

    "You are coming to terms that this is {i}not{/i} a game."
    "These computers have somehow become sentient."
    "You ask, confusedly: “Who...are you?”"
    all "..."
    pause (0.35)


    voice "audio/TI_Line8.wav"
    ti "I am a Texas Instruments 99/4A."


    voice "audio/Odyssey_Line4.wav"
    ody "I am a Magnavox Odyssey!"



    ### "but what would you like to call me?
    voice "audio/Odyssey_Line5.wav"
    voice "audio/TI_Line9.wav"
    voice "audio/Mac_Line5.wav"
    all "but what you would like to call me?"
    pause(2)

    jump a2_reset_choice

label a2_reset_choice:
    "Which computer terminal do you approach?"
    menu:
        "iMac G3":
            jump name_mac
        "TI-99/4A":
            jump name_ti
        "Magnavox Odyssey":
            jump name_ody
