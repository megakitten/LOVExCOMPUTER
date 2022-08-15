# Act 2, Meet Compute - Naming the Computers

label name_mac:
    python:
        _MacName = renpy.input(_("Name the iMac G3."))
        _MacName = _MacName.strip() or ("iMac G3")
        _MacHAL = (_MacName == "HAL9000") and (_InputName == "Dave")
    define mac = Character("[_MacName]",
    who_color="#eb6434", who_font="ChicagoFLF.ttf", who_size=40,
    what_color="#ffd182", what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_mac

label name_ti:
    python:
        _TiName = renpy.input(_("Name the TI-99/4A."))
        _TiName = _TiName.strip() or ("TI-99/4A")
        _TiHer = (_OdyName == "Samantha") and (_InputName == "Theordore")
    define ti = Character("[_TiName]",
    who_font="ChicagoFLF.ttf", who_size=40,
    what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_ti

label name_ody:
    python:
        _OdyName = renpy.input(_("Name the Magnavox Odyssey."))
        _OdyName = _OdyName.strip() or ("Magnavox Odyssey")
        _OdyElectricDreams = (_TiName == "Miles") and (_InputName == "Edgar")
    define ody = Character("[_OdyName]",
    who_font="ChicagoFLF.ttf", who_size=40,
    what_font="ChicagoFLF.ttf", what_size=27, what_slow_cps=20, what_slow_abortable=False)
    jump choose_ody

    return
