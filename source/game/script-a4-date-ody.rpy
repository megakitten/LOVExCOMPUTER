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
        "I don't really understand how you communicate...":
            jump ody_topic_network
        "What was the last dream you had?":
            jump ody_topic_dream
    return

label ody_topic_network:
    ody "ok, I love that you asked this!"
    ody "This is like the science of parties right here!"
    ody "This is how *WE* *!!CONNECT!!*"
    ody "{size=+5} THIS IS THE *rEAl* ~sTUFf~"
    ody "..."
    ody "{size=-3}...communication..."
    ody "communication is eVERYtHING!"
    ody "@@@@!!__///~*~\\\__!!@@@@@"
    ody ""
    ody "..."
    ody "."
    ody ".."
    ody "..."
    ody "So let me tell you about the network...."

    ### Describe the network!



    jump date_night

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
            jump ending_dream

label ody_dreamscape_more:


    ### more lore / narrative to the dream?


    jump ending_thoughts
