# Act 4, TI Date

label a4_date_ti:
    scene bg room

    ### show computer!!!

    ti "so, like I was saying last time, I just learn from whatever I can find on the server."
    ti "but when I try to make my own stuff, well, I just think I haven't developed my own style yet..."
    "..."
    ti "...want to see some of my art???"
    menu:
        "sure":
            jump ti_artPortfolio
        "of course!":
            jump ti_artPortfolio

label ti_artPortfolio1:
    show 0001.jpg
    "The inscription reads,"
     "
        I am told,
        ' Make a prayer,
          Make a promise to God! '

        But as I watch,
        she is typing up that very poem now,
        and I recognize myself in all the words."
    ti "..."
    you "That's really nice!"
    ti "...thanks. I appreciate that a lot."
    jump ti_question

label ti_artPortfolio2:
    show 0004.jpg
    "The inscription reads,"
    "
        For the first time in my life, I had a real live robot that I could control.
        It was my own.
        I could make it do whatever I wanted.
        My own pet."
    ti "..."
    "That's really nice!"
    ti "...thanks. I appreciate that a lot."
    jump ti_question

label ti_question:
    ti "Can I ask you a question?"
    "Sure!"
    ti "Am I really just a tool for you to use?"
    "...I don't know how to answer that..."
    ###Bell triple ding
    jump date_end







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


label ti_question:
    pause(1.0)
    ody "Do you ever feel lonely? Like..."
    ody "Like, you feel like you are the only one online?"
    ody "Like you are just a copy of a shell of a being?
