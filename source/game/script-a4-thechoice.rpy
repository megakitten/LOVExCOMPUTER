# Act 3, The Choice

label date_night:
    "..." # key in door?
    "You unlock the door for what feels like the millonth time."
    "You great the familiar basement smell."
    scene bg room

    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft

    "Who do you want to get to know better?"
    menu:
        "[_MacName]":
            jump date_mac
        "[_TiName]":
            jump date_ti
        "[_OdyName]":
            jump date_ody

label a3_thechoice:

    # storm sfx, use Andes recordings

    "You hope campus PD doesn't write you a ticket..."
    "..." ### sfx of key in door?
    "You unlock the door for what feels like the millonth time."
    "You great the familiar basement smell."
    scene bg room

    show macFront at macTop
    show ti15 at tiRight:
        xalign 1.05
    show ody45 at odyLeft

    "Who do you want to get to know better?"

    menu:
        "[_MacName]":
            jump date_mac
        "[_TiName]":
            jump date_ti
        "[_OdyName]":
            jump date_ody

    return
