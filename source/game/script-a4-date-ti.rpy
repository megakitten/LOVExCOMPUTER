# Act 4, TI Date

label a4_date_ti:
    scene bg room
    e "Date TI"

    #Make this question come from you
    #you can pick whether:
        #    1. to ask about MIL
        # or 2. about language (BASIC)
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

    ## Brief Date Draft ##
    # Shows you AI poetry
    # Talks about learning and pattern finding
    # Talk about loops and repeats and resonances
    # You talk about loneliness
    # As you start to get into it,, the power blows
    # IF YOU NAMED IT “HAL” OR “HAL9000”, the power doesn’t blow but the the house starts coming for you, then you hear TI’s voice.
    # Ending Credits

    # OR #

    # they just want to listen to music together with you.
        # play one of andy's tracks (HCI if not in the game pack)
    # starts talking about the world it imagines when it makes this music
    # a place called the wired.
    # everyone is connected
    # "its perfect"
    #  $VERY SCARY!$ wouldn't you like to join?
    ## POWER SURGE ##

    return
