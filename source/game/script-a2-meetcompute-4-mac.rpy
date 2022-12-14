# Act 2, Actual Conversations

###CLIP ART AND PROGRAMMING MANUALS

label choose_mac:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show macFront

    ### " late at night, do you get that feeling? the feel that you have to create something? "
    voice "audio/Mac_line6.wav"
    
    pause(1.0)
    mac "I wanted to ask you..."
    mac "like...late at night"
    mac "do you ever get that feeling?"
    mac "That feeling that you just *HAVE* to *CREATE* something?"
    ### Flash Screen with AI ###
    pause(1.0)
    mac "I feel that way a lot..."
    mac "..."
    mac "You know what..."
    mac "I'm gunna show you some of my art!"
    mac "I've been really inspired lately!"
    mac "So..."
    mac "...do want to see some of my art?"
    menu:
        "i guess":
            jump mac_artPortfolio1
        "of course!":
            jump mac_artPortfolio2

label mac_artPortfolio1:
    show art1
    "The accompanying text reads,"
    "I was told,
    ' Make a prayer, '
    and ' Make a promise to God! '

    But as I watch,
    She is typing up that very poem now,
    and I recognize myself in all the words."
    pause(4)
    jump mac_artReaction

label mac_artPortfolio2:
    ### replace image
    show art2
    "The accompanying text reads,"
    "For the first time I had my very own robot. I could make it do whatever I wanted. My pet."
    jump mac_artReaction

label mac_artReaction:
    mac "..."
    you "That's really nice!"
    mac "...thanks. I appreciate that a lot."
    jump mac_question

label mac_art_portfolio:

    ### somehow display some ai gen pix/vids
        # --> slowly getmacng closer to figures

label mac_question:

    mac "Can I ask you a question?"
    "Sure!"
    mac "What makes us so different?"
    "..."
    ###Bell triple ding sfx
    jump date_night
