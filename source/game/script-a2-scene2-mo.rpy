# Act 2, Scene 2, MO Path

label chooseMo:
    scene mal 00 with Dissolve(1)
    show mo45 at tiSpot
    mo "Hey..."
    mo "Why is it called the Media Intervention Lab?"

    menu:
        "Because we intervene in media technologies.":
            you "Because we intervene in media technologies."
            you "Digitize them and connect them into a network."
            jump moAct2Scene3b

        "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\"":
            you "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\""
            you "But then they got absorbed into the College of Communications Technology and the mission changed."
            you "Now its all about digitizing and networks."
            you "You should have access to the old stuff about the lab through the network. Let me know if you can’t find them."
            jump moAct2Scene3a

label moAct2Scene3a:
    #?

label moAct2Scene3b:
    #?

    return
