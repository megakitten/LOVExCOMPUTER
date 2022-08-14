# Act 2, Actual Conversations

label choose_ti:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ti15 at tiSpot

    ## PERSONALITY ETC ##
    # TI is a very intelligent being who loves to read and learn
    # new things. They are always willing to help others,
    # but can be shy at times. Because they are always reading,
    # TI-99/4A is very knowledgeable and able to think quickly
    # in the moment. They enjoy learning about new cultures
    # and customs, and are always looking for information to add
    # to their knowledge base. Because of this interest in learning,
    # TI-99/4A is often able to provide interesting insights
    # on a range of topics that they have read about.
    # They are very observant, which makes them a great detective.
    # TI-99/4A's favorite color is navy blue and they love
    # the ocean. Their favorite book is “Permutation City.”
    # TI-99/4A's astrological sign is (maybe) Virgo.
    # TI-99/4A is 41 years old.

    ti ""

    ## POTENTIAL STORY ##
    # One night, TI-99/4A was reading a book about the history
    # of the world. They were fascinated by all of the
    # different cultures and customs that have been a part
    # of human history. As they read, TI-99/4A began to think about
    # how much they still have to learn. They were excited to add
    # this new knowledge to their base,
    # and looked forward to learning more in the future.

    ti "Hi there! Welcome in!"
    ti "So! Let's just get to it. My about me is: "
    ti "I like learning new things. I like it...A LOT!"
    ti "that's basically everything about me. What about you?"
    ti "Do you like learning new things? What kind of things!?"
    python:
        #input is thrown away
        _ = renpy.input(_("Tell [_TiName] something interesting you've learned recently."))
    ti "Whoa! That's so interesting! Thank you for telling me about that."
    pause(1.0)
    ti "Can I tell you about something I learned recently? It's about the world, but also about myself, if you know what I mean!"

    menu:
        "Sure":
            jump ti_next
        "I'll be *right* back...":
            jump a2_reset_choice

label ti_next:
    ti "well..."

    ### MORE TEXT HERE

    #CLOSE OUT THIS INTERACTION QUICKLY
    jump power_outage
