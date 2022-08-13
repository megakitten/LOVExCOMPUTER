# Act 2, Actual Conversations

label choose_mac:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show macFront

    

    ## PERSONALITY ETC ##
    # Mac is creative, innovative, and individualistic
    # but also a bit nervous and emotionally fragile.
    # They are into art and they have a passion for helping others.
    # G3 is an Aquarius. Their favorite activities are usually
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

    #Old Draft Question - TAKE IT OR LEAVE IT
    mac "Hey..."
    mac "Why is it called the Media Intervention Lab?"
    menu:
        "Because we intervene in media technologies.":
            you "Because we intervene in media technologies."
            you "Digitize them and connect them into a network."

            #jump reset_choice

        "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\"":
            you "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\""
            you "But then they got absorbed into the College of Communications Technology and the mission changed."
            you "Now its all about digitizing and networks."
            you "You should have access to the old stuff about the lab through the network. Let me know if you can’t find them."

            #jump reset_choice


    jump reset_choice
