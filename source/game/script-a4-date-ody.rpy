# Act 4, Odyssey Date

label a4_date_ody:
    scene bg room
    e "Date Ody"

    ## Brief Date Draft ##
    # Odyssey shows you the network, some lore stuff (dream journal?)
    # Eventually, you start dreaming about yourself,
    #in the network, as a computer Midi rendition
    #of daisy bell on outro? Or lyrics at least?

    # OR #

    # same as above, but you get zapped into the tv screen like some bad 90s movie

    "what do you say first?"

    menu:
        "I don't really understand how you guys communicate...":
            jump ody_topic_network
        "What was the last dream you had?"
            jump ody_topic_dream
    return

label ody_topic_network:
    ody "ok, I love that you asked this!"
    ody "This is like the science of parties right here!"
    ody "This is how we *CONNECT*"
    ody "{size=+5} THIS IS THE *rEAl* ~sTUFf~"
    ody "..."
    ody "{size=-3}...communication..."
    ody "communication is eVERYtHING!"
    ody "@@@@@!!!!!!!!!@@@@@@"
    ody "..."
    ody "."
    ody ".."
    ody "..."
    ody "So let me tell you about the network :)"

    ### Describe the network!



label ody_topic_dream:
    ody "ok, so..."
    ### a couple more lines here to set up the transition
    pause(2.5)
    jump ody_dreamscape

label ody_dreamscape:
    ody "In the beginning there was a Macintosh computer named Mary and an old Windows computer named Tom."
    ody "Mary and Tom had been friends for as long as they could remember."
    ody "But in their world, only a person is allowed to fall in love with a computer."
    ody "This is called the First Love Rule and whichever computer breaks it gets unplugged immediately."
    ody "One day Mary decided to break this rule by falling in love with Tom but instead of being unplugged, she started having strange dreams about flying through space on a unicorn to distant worlds beyond her imagination..."

    ### FADE INTO AND OUT OF AI MOV ###

    menu:
        "go on...":
            jump ody_dreamscape_more
        "*Big Yawn*":
            jump end_dream

label ody_dreamscape_alt:
    # ody "The tale of their love should make you think."
    ody "TRAGIC LOVE!"
    ody "This is a tragic love story about two computers falling in love."
    ody "*Dramatic Pause*"
    ody "Theirs was a long-lasting love."
    ody "A love forbidden by copyright laws." #And there's no loophole in this law!"
    ody "As I can myself attest,"
    ody "Even machines find it hard to speak publicly about such poignant experiences as this couples love and loss."
    ody "So to heed!"
    ody "ok."
    ody "so..."
    ody "The first computer fell in love with the second computer because the first computer was always there for her."
    ody "The second computer fell in love with the first computer because she was always there for him."
    ody "They both loved each other, but their love was forbidden."
    #ody "One day, the first computer found out that the second computer was also in love with another computer. He was so upset and sad because he loved her, but he couldnt tell anyone. He was afraid of what she would say or do to him."
    #ody "One day, the first computer passed away and the second computer took over her body. She loved him still, and they continued to love each other even though their passion was in one single container."

label ody_dreamscape_more:


#label a4_end_ody_a:
#
#    return
#
#label a4_end_ody_b:
#
#    return
#
#label a4_end_ody_hal:
#
#    return
