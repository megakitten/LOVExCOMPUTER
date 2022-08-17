# Act 2, Meet Compute

label a2_meetcompute_intro:
    play music "audio/MeetCompute_TheChoice.mp3"
    scene mal 00 with Dissolve(1)

    ### storm sfx, use Andes recordings

    "It's raining. Hard."
    "You park on the street outside of the MIL."
    "You hope campus PD doesn't write you a ticket..."
    "..." # key in door?
    "The familiar basement smell greats you."
    show macFront
    "You are sitting in front of the iMac G3 with your laptop and an external CD drive, digitizing “If Monks Had Macs.”"
    with hpunch
    "You hear something behind you."
    ### "h. h. hi."
    "Could it be... {w}a voice?{\w}"
    ### "hi"
    scene mal 01 with Dissolve(0.5)
    show ody45 at odyLeft
    show ti15 at tiRight
    "You turn around and look at the desk holding the TI99 and Magnavox Odyssey."
    "You think nothing of it and turn back around."
    scene mal 00 with Dissolve(0.5)
    show macFront
    with hpunch
    "Then you hear it again, unmistakably a voice."
    ### "hello."
    "{w}But, a computer’s voice.{\w}"
    "Before you turn around, you know the source."
    scene mal 01 with Dissolve (0.5)
    show ti15 at tiSpot
    "The TI-99 and its accompanying screen sit stoically, in near silence. Only the whine of the monitor permeates the silence."
    "Could you have just imagined the voice? After all, you do already know the sound of the TI-99’s voice."
    "You did spend 3 nights painstakingly recording every phoneme produced by the speech synthesis module..."
    with hpunch
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.15)
    hide 0009
    pause (0.15)
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.35)
    hide 0009
    "But then the screen flickers and a voice crackles from the speaker."
    ti "Hi!!!! What’s your name!?"
    "You say your name." #{w}You wait, with unexpected apprehension.{\w}"
    #"..."
    #"Nothing happens."
    #"You consider the fact that this computer does not have a microphone."
    "You approach the computer."
    #Image zoom in here
    "You type your name."
    python:
        _InputName = renpy.input(_("Input your name."))
        _InputName = _InputName.strip() or ("Tetsuo")
    define you = Character("[_InputName]")
    ti "Input your pronouns."
    "You type your pronouns."
    python:
        _InputPronoun = renpy.input(_("Input your pronouns."))
        _InputPronoun = _InputPronoun.strip() or ("&amp")
    #define z = Character("[_InputPronoun]")
    with hpunch
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.15)
    hide 0009
    pause (0.15)
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.35)
    hide 0009
    #"The computer spits out an error messages along with an unfriendly beep."
    #ti "Try again."
    "*SUCCESS SOUND EFFECT*"
    with hpunch
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.15)
    hide 0009
    pause (0.15)
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.35)
    hide 0009

    ti "User! Hello!"
    with hpunch
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    pause(0.15)
    hide 0009
    show 0001 at center:
        zoom 1.9
    pause (0.15)
    hide 0001
    show 0009 at center:
        zoom 1.9
    pause(0.35)
    hide 0009
    show 0001 at center:
        zoom 1.9
    pause (0.35)
    hide 0001
    show 0009 at center:
        zoom 1.9
    pause(0.35)
    hide 0009
    show ti15 at tiRight
    show ody45 at odyLeft
    with hpunch
    "Then the Magnavox Odyssey’s screen flickers to life."
    ody "User! Hello!"
    "You are now supremely confused."
    with hpunch
    show 0009 at center:
        zoom 1.9
    pause(0.15)
    hide 0009
    show 0001 at center:
        zoom 1.9
    pause (0.15)
    hide 0001
    show 0009 at center:
        zoom 1.9
    pause(0.35)
    hide 0009
    hide ti15
    hide ody45
    show 0001 at center:
        zoom 1.9
    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft
    "The screens of each computer become wavy and distorted."
    show my_movie
    "The voices, including the G3, start talking over each other building to a crescendo, then the screen goes black."
    scene black
    "You have passed out, overwhelmed by the realization that these computers are sentient."

    ### space for the starry night video perhaps? ###

    #Not sure if this is supposed to be included or not (below)
    #DREAM SEQUENCE about the computers? [dont have to do this yet. Just an idea]
    #When you wake up, the computers are chatting among themselves, the text of their speech displaying on their respective screens.
    #This is when you have the choice of which computer to romance. [Choice: G3, Odyssey, TI99]

    jump a2_meetcompute_conversation

    return
