# Act 2, Actual Conversations

label choose_ody:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ody45 at tiSpot

    ## PERSONALITY ETC ##
    # is a playful and curious soul who loves to explore
    # new activities. They are energetic, outgoing and
    # love hosting parties. They are creative and have a knack
    # for coming up with new ideas. They are also independent
    # and can be a bit of a rule breaker,
    # while maintaining a perpetually positive attitude.
    # Magnavox Odyssey’s favorite color is green and favorite
    # book is Riplies Believe It or Not. Their astrological sign
    # is (maybe) Pisces. Odyssey is (CurrYear - 1972) years old.

    ody "Hey..."
    ody "So what's your story? Tell me everything"
    ody "I've been told that I'm a good listener!"
    ody "I'm actually training to be a therapist."
    ody "..."
    ody "Let it all out!"
    ody "...uh...please"
    python:
        #input is thrown away
        _ = renpy.input(_("Tell [_OdyName] your deepest darkest worries."))
    ody "damn..."
    ody "i really feel that"


    ### Flash Screen with AI ###

    ody "I felt that way. But then I went and got everyone together."
    ody "A. BIG. ASS. {size=+7}LAN. PARTY!."
    ody "{size=-7} IT wuz {size=+2}uh{size=+7} F*(&ing Cl4ssic!"

    menu:
        "*Bell dings*":
            ody "Oh. I guess that's our time! It was really nice meeting you!"
            jump ody_leave
        "YOURE A LEGEND!":
            jump ody_next
        "omfg tell me more":
            jump ody_moreInfo

label ody_leave:
    menu:
        "I'll be *right* back...":
            jump a2_reset_choice
        "hope you have another party soon! seems like a jam!":
            jump ody_next

label ody_moreInfo:
    ### add content here if time

    ## INCOMPLETE STORY IDEAS ##
    # One night, Magnavox Odyssey went to a LAN party
    # and had the best time! They met so many new folks and
    # gyrated until they couldn't move anymore.
    # libi had to come in and fix them the next.

    # is odysessy high-key poly?

    jump ody_next

label ody_next:
    "*Bell dings*":
    ody "Oh. I guess that's our time! It was really nice meeting you!"
    jump power_outage
