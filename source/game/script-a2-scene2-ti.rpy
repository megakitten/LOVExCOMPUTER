# Act 2, Scene 2, TI Path

label chooseTi:
    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show ti15 at tiSpot
    ti "Hey..."
    ti "Why is it called the Media Intervention Lab?"

    menu:
        "Because we intervene in media technologies.":
            you "Because we intervene in media technologies."
            you "Digitize them and connect them into a network."
            jump tiAct2Scene3b

        "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\"":
            you "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\""
            you "But then they got absorbed into the College of Communications Technology and the mission changed."
            you "Now its all about digitizing and networks."
            you "You should have access to the old stuff about the lab through the network. Let me know if you can’t find them."
            jump tiAct2Scene3a

label tiAct2Scene3a:
    #?

label tiAct2Scene3b:
    #?

    return
