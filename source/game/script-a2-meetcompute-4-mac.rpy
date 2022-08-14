# Act 2, Actual Conversations

label choose_mac:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show macFront

    ## PERSONALITY ETC ##
    # Mac is creative, innovative, and individualistic
    # but also a bit nervous and emotionally fragile.
    # They are into art and they have a passion for helping others.
    # G3 is (possibly) an Aquarius. Their favorite activities are all
    # art-related, and they are always looking for ways
    # to improve the world around them.
    # They can be overly idealistic
    # and they can become detached from reality at times.
    # They like to read old design books on color theory and stuff.
    # Their favorite color is light blue, and their favorite food
    # is salmon. G3 is 24

    ##  POTENTIAL STORY ##
    # One night, iMac G3 was browsing an art museum catalog
    # and saw a painting called "Aquarius."
    # They felt a strong connection to it and secretly hoped that
    # others saw them like the figure in the painting.
    # G3 decided they wanted to become an artist too,
    # and started using MAL’s software library to create digital art.
    # She also became involved in several charities
    # that help improve the world for Aquarii.

    mac "Hi again!"


    ### SAY MORE THINGS HERE"


    python:
        #input is thrown away
        _ = renpy.input(_("Tell [_MacName] your last good dream."))
    mac "That makes me really happy. Thank you for sharing that with me!"
    pause(1.0)
    mac "I wanted to ask you..."
    mac "like...late at night, do you ever get that feeling?"
    mac "That feeling that you just *HAVE* to *MAKE* something?"


    ### Flash Screen with AI ###


    mac "I feel that way a lot..."

    menu:
        "that's cool...":
            jump mac_leave
        "Wow, that's fascinating":
            jump mac_next
        "omfg me too! tell me more!":
            jump mac_moreInfo

label mac_leave:
    menu:
        "ok, im still into this":
            jump mac_next
        "I'll be *right* back...":
            jump a2_reset_choice

label mac_moreInfo:


    ### add content here if time


    you "how often do you feel that way?"
    mac "oh! well like...all the time, really!"
    jump mac_next


label mac_next:
    ###

    CLOSE OUT THIS INTERACTION QUICKLY


    jump power_outage
