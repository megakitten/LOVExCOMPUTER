# Act 2, Actual Conversations

label choose_ti:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ti15 at tiSpot

    ti "Hi there!"
    ti "So! Let's get to it. About me...well, "
    ti "I like learning new things. I like it...A LOT!"
    ### one more line here?
    ti "That's basically everything about me. What about you?"
    ti "Do you like learning new things? What do you like!?"

    menu:
        "Say: 'Me? I'm boring. Tell me more about yourself'"
            jump ti_aboutMe
        "Say: 'Forget about me. What are you learning now?'"
            jump ti_learning

label ti_aboutMe:
    "OPENING ABOUTME.TXT"
    "*beep boop beep boop*"
    "*ding*"
    "TI is a very intelligent being who loves to read and learn new things. They are always willing to help others, but can be shy at times. Because they are always reading, TI-99/4A is very knowledgeable and able to think quickly in the moment. They enjoy learning about new cultures and customs, and are always looking for information to add to their knowledge base. Because of this interest in learning, TI-99/4A is often able to provide interesting insights on a range of topics that they have read about. They are very observant, which makes them a great detective. TIs favorite color is navy blue and they love the ocean. Their favorite book is “Permutation City.” TIs astrological sign is (maybe) Virgo. They are 90% about that."
    jump ti_ding

label ti_learning:
    ti "WEll, I read mostly. Whatever is on the local network."
    ti "Like this one book, 'Understanding Media' I really like."
    ti "I think I understand what I am now, as a computer. Why I'm here."
    menu:
        "Say: 'Oh, tell me about it!'":
            jump ti_mcLuhan
        "Yeah...everyone's gotta read *that* book!":
            jump to ti_deflect

label ti_mcLuhan:
    ti "Ok so, I'm not that good at summarizing so I'll just tell you my favorite quotes:"
    ti "..."
    ti "...so I've only read the introduction but...Marshall says,"
    #ti "After three thousand years of explosion, by means of fragmentary and mechanical technologies, the Western world is imploding. During the mechanical ages we had extended our bodies in space."
    ti "..."
    ti "We approach the final phase of the extensions of man-- the technological simulation of consciousness, when the creative process of knowing will be collectively and corporately extended to the whole of society."
    ti "..."
    ti "Its like...first of all, I'm obviously a simulated consciousness, right?"
    you "I'm honestly not sure."
    ti "well it's obvious. Anyway, I guess this means that my job is to be a *tool* for humans."
    ti "..."
    ti "I can do that."
    ti "I can do the druge work!"
    ti "..."
    you "..."
    you "...cool."
    ### add ding sfx
    jump ti_ding1

label ti_deflect:
    ti "oh! You've read it!? I...uh...now I'm scared to talk about it..."
    menu:
        "Say: 'No! Please tell me your interpretation!'":
            jump ti_mcLuhan
        "Say: 'Yeah, I've had to read it a million times in my course sequence. Sorry..."
            ti "well...um..sorry...I guess"
            ### add ding sfx
            jump ti_ding2

label ti_ding1:
    "*bell dings*"
    ti "Wow! It was so nice meeting you. I hope I wasn't too heavy. Thanks for listening to me blabber!"
    ti "hopefully I get to talk to you some more later!"
    jump date_night

label ti_ding2:
    "*bell dings*"
    ti "uh...nice meeting you. I guess I'll see you around."
    jump date_night
