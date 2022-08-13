# Act 2, Meet Compute - Naming the Computers

label name_mac:
    python:
        _MacName = renpy.input(_("Name the iMac G3."))
        _MacName = _MacName.strip() or ("iMac G3")
        _MacHAL = _MacName == "HAL9000"
    define mac = Character("[_MacName]",
    who_color="#eb6434", who_font="ChicagoFLF.ttf", who_size=40,
    what_color="#ffd182", what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_mac

label name_ti:
    python:
        _TiName = renpy.input(_("Name the TI-99."))
        _TiName = _TiName.strip() or ("TI-99")
        _TiHAL = _TiName == "HAL9000"
    define ti = Character("[_TiName]",
    who_font="ChicagoFLF.ttf", who_size=40,
    what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_ti

label name_ody:
    python:
        _OdyName = renpy.input(_("Name the Magnavox Odyssey."))
        _OdyName = _OdyName.strip() or ("Magnavox Odyssey")
        _OdyHAL = _OdyName == "HAL9000"
    define ody = Character("[_OdyName]",
    who_font="ChicagoFLF.ttf", who_size=40,
    what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_ody

    return

label reset_choice:
    scene mal 00 with Dissolve(1)
    "You ask, confusedly: “What do I call you?”"
    all "I don't know..."
    all "Please tell me what you would like to call me."
    "Select which computer to name."
    menu:
        "iMac G3":
            jump name_mac

        "TI-99/4A":
            jump name_ti

        "Magnavox Odyssey":
            jump name_ody
