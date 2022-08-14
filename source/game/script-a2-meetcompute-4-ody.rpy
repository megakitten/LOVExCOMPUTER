# Act 2, Actual Conversations

label choose_ody:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ody45 at tiSpot

#    menu:
#        you "So tell me about yourself"
#
#        you "What's the last dream you had?"
#
#
#    menu:
#        "Wow, that's fascinating":
#            jump mac_next
#        "omfg me too! tell me more!":
#            jump mac_moreInfo

    ### ODY TELLS YOU ABOUT THE LOCAL NETWORK AND HOW ITS JUST A BIG PARTY

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

    ### Flash Screen with AI ###
    ody "Do you ever feel lonely? Like..."
    ody "Like, you feel like you are the only one online?"
    ody "Like you are just a copy of a shell  script of a being?"
    ody "I felt that way."
    ody "But then I went and got everyone together."
    ody "A BIG. ASS. {size=+7}LAN. PARTY!."
    ody "{size=-7} IT wuz {size=+2}uh{size=+7} F*(&ing Cl4ssic!"

    menu:
        "That sounds awesome! YOU ARE A LEGEND!":
            jump ody_next
        "omfg tell me more":
            jump ody_moreInfo



label ody_moreInfo:
    ### add content here if time
    ody "I made so many new connections!"
    ody "I probably know everyone in this place now!"
    ody "We swapped files like there was no tomorrow. There's nothing like it. That speed..."
    ody "It's all because of that local area network. That's where the party is *really* at."
    you "Yeah, sounds like you are totally wired in."
    ody "Yeah."
    ody "..."
    ody "I like that...'The Wired'. That's what I'll call my party domain."
    ody "You are welcome in The Wired anytime, of course!"
    you "Nice!"
    jump ody_next

label ody_next:
    "*Bell dings*"
    ody "Oh. I guess that's our time! It was really nice meeting you!"
    jump date_night

label ody_leave:
    menu:
        "I'll be *right* back...":
            jump a2_reset_choice
        "hope you have another party soon! seems like a jam!":
            jump ody_next
