# Act 4, The Choice

label date_night:
    "..." # key in door?
    "You unlock the door for what feels like the millonth time."
    "You greet the familiar basement smell."

    ### new room, vinyl?

    scene mal date

    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft

    "Who do you want to get to know better?"
    menu:
        "[_MacName]":
            #jump date_mac
            jump power_outage
        "[_TiName]":
            #jump date_ti
            jump power_outage
        "[_OdyName]":
            #jump date_ody
            jump power_outage
