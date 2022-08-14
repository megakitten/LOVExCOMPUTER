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
        "Alexa! Order a copy of"



label ending_dream:
    # ODYSSEY ENDING 1
    ### you go back to your IoT house
    ### you have the "ROBOT DREAM"

label ending_thoughts:
    # ODYSSEY ENDING 2
    ### thoughts about "being gay for my computer"
    ### fall asleep and either see a nice ai mov or another text dream.
    ### wake up and get ready to tell odyssey your updated thoughts about computers and humans

##########################
## TI POSSIBLE SECTIONS ##
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


label ti_question_alt:
    pause(1.0)
    ody "Do you ever feel lonely? Like..."
    ody "Like, you feel like you are the only one online?"
    ody "Like you are just a copy of a shell of a being?"

label mac_dialogue:

    mac "but when I try to make my own stuff, well, I just think I haven't developed my own style yet..."
    "..."

## Brief Date Draft ##
# Art stuffs Eventually, asks you why humans treat
# humans like this.
# Use My Computer Likes Me when I speak BASIC stuff
# as evidence
# You go home to your IoT-enabled automated house,
# and get an electronic backrub.
# You forget all about the stresses of the day.
# The budding realizamacon that your relamaconship
# with technology is enmacrely f’ed does not bother
# you for now.

#  Bliss overtakes you as your muscles are vibrated
#  according to a programmed sequence.
# If you think about it more, (or chose not to),
# the power blows and your house falls into darkness.
# The silence is somewhat frightening…

## OR ##
# mac tells its story/interests
# you look at clip art and mac
# shows you their generamacve art

# mac ponders the idenmacty of the armacst
# asks, if making an impact on the world
# is the way to define a real life?
# you say:
    # of course not. all sorts of digi life is poss
    # theres plenty of people alive who haven't had an impact!
# mac asks, are we just servants to you?
    # shows my computer likes me when i speak BASIC as evidence
# you squirm out of the quesmacon, and eventually head home

# When you are home, in your IoT pad,
# do you think more about it?
    # no, you float off into rumbling massage bliss (vibrates bg/imgs)
    # yes, you alexa-search "what is the relamaconship between man and computer?"
        # returns marshall mcluhan
        # reads intro to Understanding Media (most of the first paragraph)
        # you drift off to a deep but troubled sleep


#######################
## Weird Ody Dialogue##
    ody "Hey..."
    ody "So what's your story? Tell me everything"
    ody "I've been told that I'm a good listener!"
    ody "I'm actually training to be a therapist."
    ody "..."
    ody "Let it all out!"
    ody "...uh...please"
    python:
        #input is thrown away
        _ = renpy.input(_("Tell [_OdyName] your deepest darkest worries."))
    ody "damn..."
    ody "i really feel that"

########################
### Mac Story for intro#

    ##  POTENTIAL STORY ##
    # One night, iMac G3 was browsing an art museum catalog
    # and saw a painting called "Aquarius."
    # They felt a strong connection to it and secretly hoped that
    # others saw them like the figure in the painting.
    # G3 decided they wanted to become an artist too,
    # and started using MAL’s software library to create digital art.
    # She also became involved in several charities
    # that help improve the world for Aquarii.
