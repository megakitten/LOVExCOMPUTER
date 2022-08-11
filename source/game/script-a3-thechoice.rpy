# Act 3, The Choice

label a3_thechoice:
    # storm sfx, use Andes recordings
    e "It's raining. Hard."
    e "You park on the street outside of the MIL."
    e "You hope campus PD doesn't write you a ticket..."
    e "..." # key in door?
    e "You unlock the door for what feels like the millonth time."
    e "The familiar basement smell greats you."
    scene bg room

    #steal code from the other choice moment in a2

    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft

    ### <MISSING TEXT> ###

    "Who do you want to get to know better?"
    menu:
        _MacName:
            jump date_mac

        _TiName:
            jump date_ti

        _OdyName:
            jump date_ody

    return
