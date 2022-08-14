### This is where text goes to die and hopefully live a happy afterlife in another project

### NARRATIVE/l0gIc FOR WEIRD PRONOUN INTERACTION with ti 99
label ti99_pronounError:
    ##a2 ti scene
    "And again."
    with hpunch
    hide ody15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.15)
    hide 0009
    pause (0.15)
    hide ti15 at tiSpot
    show 0009 at center:
        zoom 1.9
    show ti15 at tiSpot
    pause(0.35)
    hide 0009
    "Each time the same result."
    "Finally you receive a hint. And you realize you must input your name as “User”."

    $ userName = ""
    while userName != "user" and userName != "User":
        python:
            userName = renpy.input(_("Input your name."))
            userName = userName.strip()

###
label unsaved_user_input:
    python:
        #input is thrown away
        _ = renpy.input(_("Tell [_TiName] something interesting you've learned recently."))

label ti_weirdResponse:
    ti "Whoa! That's so interesting! Thank you for telling me about that."
    pause(1.0)
    ti "Can I tell you about something I learned recently?"
    ti "It's about the world, but also about myself, if you know what I mean!"

label ti_unsure:
    #Make this question come from you
    #you can pick whether:
        #    1. to ask about MIL
        # or 2. about language (BASIC)
    ti "Hey..."
    ti "Why is it called the Media Intervention Lab?"
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

label ti_weirdDialogue:
    ti "Am I real?"
    "Yes, of course!"
    ti "I don't believe you. And I'm sad now."

########################
### POSSIBLE ENDINGS ###
########################
label ending_outage:
    # POWER OUTAGE SHORT ENDING

    ### flicker to black, thunder clap, tree fall, electric shock and digital sizzle sounds

    "This is the last time you ever talk to this strange trio of computers."
    "Someone at the lab fixed their power sources that power surge."
    "As you sit with your feet up, roomba happily humming by..."
    menu:
        #In a computer voice
        "*Look at apple watch* I am so grateful for technology! I LOVE COMPUTERS!":


            ### ^^play render of the above line^^
            ### extremely long dissolve to black

            jump credits
        "Alexa! Order a copy of



label ending_dream:
    # ODYSSEY ENDING 1
    ### you go back to your IoT house
    ### you have the "ROBOT DREAM"

label ending_thoughts:
    # ODYSSEY ENDING 2
    ### thoughts about "being gay for my computer"
    ### fall asleep and either see a nice ai mov or another text dream.
    ### wake up and get ready to tell odyssey your updated thoughts about computers and humans
