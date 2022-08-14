# Act 4, Mac Date

label a4_date_mac:
    scene bg room
    show macFront
    pause(1.0)
    mac "I wanted to ask you..."
    mac "like...late at night, do you ever get that feeling?"
    mac "That feeling that you just *HAVE* to *MAKE* something?"
    ### Flash Screen with AI ###
    pause(1.0)
    mac "I feel that way a lot..."
    mac "You know what..."
    mac "I'm gunna show you some of my art!"
    mac "Maybe it will inspire you! I've been really inspired lately"
    mac "so...want to see some of my art???"
    menu:
        "sure":
            jump mac_artPortfolio1
        "of course!":
            jump mac_artPortfolio2

label mac_artPortfolio1:
    show 0001.jpg
    "The accompanying text reads,"
     "
        I was told,
        ' Make a prayer,
          Make a promise to God! '

        But as I watch,
        She is typing up that very poem now,
        and I recognize myself in all the words."
    jump mac_artReaction

label mac_artPortfolio2:

    ### replace image
    show 0004.jpg

    "The accompanying text reads,"
    "It was my own. I could make it do whatever I wanted. My own pet."
    jump mac_artReaction

label mac_artReaction:
    mac "..."
    you "That's really nice!"
    mac "...thanks. I appreciate that a lot."
    jump mac_question

label mac_art_portfolio:

    ### somehow display some ai gen pix/vids
        # --> slowly getmacng closer to figures

label mac_questions:

    mac "Can I ask you a question?"
    "Sure!"



    mac "Aren't we both artists? What makes us so different"
    "I never said I was an artist"
    ###Bell triple ding sfx
    jump date_end
