# Act 2, Scene 2, Mac Path

label chooseMac:
    scene mal 00 with Dissolve(1)
    show macFront
    mac "Hey..."
    mac "Why is it called the Media Intervention Lab?"

    menu:
        "Because we intervene in media technologies.":
            you "Because we intervene in media technologies."
            you "Digitize them and connect them into a network."
            jump macAct2Scene3b

        "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\"":
            you "Well, it used be called the Media Archaeology Lab. It was some \"feminist science lab thing...\""
            you "But then they got absorbed into the College of Communications Technology and the mission changed."
            you "Now its all about digitizing and networks."
            you "You should have access to the old stuff about the lab through the network. Let me know if you can’t find them."
            jump macAct2Scene3a

label macAct2Scene3a:
    #?

label macAct2Scene3b:
    #?

    return
