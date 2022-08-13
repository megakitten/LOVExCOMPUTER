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

#------------------------------------------------------------------

label choose_ti:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ti15 at tiSpot
    ti ""

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
    # TI-99/4A's astrological sign is Virgo.
    # TI-99/4A is 41 years old.

    ## POTENTIAL STORY ##
    # One night, TI-99/4A was reading a book about the history
    # of the world. They were fascinated by all of the
    # different cultures and customs that have been a part
    # of human history. As they read, TI-99/4A began to think about
    # how much they still have to learn. They were excited to add
    # this new knowledge to their base,
    # and looked forward to learning more in the future.

    jump reset_choice

#------------------------------------------------------------------

label choose_ody:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ody45 at tiSpot
    ody "Hey..."
    ody ""

    ## PERSONALITY ETC ##
    # is a playful and curious soul who loves to explore
    # new activities. They are energetic, outgoing and
    # love hosting parties. They are creative and have a knack
    # for coming up with new ideas. They are also independent
    # and can be a bit of a rule breaker,
    # while maintaining a perpetually positive attitude.
    # Magnavox Odyssey’s favorite color is green and favorite
    # book is Riplies Believe It or Not. Their astrological sign
    # is Pisces. Odyssey is (CurrYear - 1972) years old.

    ## INCOMPLETE STORY IDEAS ##
    # One night, Magnavox Odyssey went to a LAN party
    # and had the best time! They met so many new folks and
    # gyrated until they couldn't move anymore.
    # libi had to come in and fix them the next.
    # Just before they were unplugged,

    jump reset_choice
