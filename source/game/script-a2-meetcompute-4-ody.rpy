# Act 2, Actual Conversations

label choose_ody:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ody45 at tiSpot

    ### " Do you ever feel lonely? Like the only one online? "
    voice "audio/Odyssey_line6.wav"

    ### Flash Screen with AI ###
    ody "Do you ever feel lonely? Like..."
    ody "Like, you feel like you are the only one online?"

    ### " Like a copy of a shell  script of a being? "
    voice "audio/Odyssey_line6.wav"
    
    ody "Like you are just a copy of a shell  script of a being?"
    ody "I felt that way."
    ody "But then I went and got everyone together."
    ody "A BIG.{size=+9} FRIGGEN.{/size}{size=+7} LAN.{/size}{size=+9} PARTY!.{/size}"
    ody "{size=-3} IT {/size}wuz {size=+2}uh{/size}{size=+7} F*(&ing Cl4ssic!{/size}"

    menu:
        "I mean, don't you ever feel alone in a crowded room though?":
            jump ody_next
        "omg tell me everything!":
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
