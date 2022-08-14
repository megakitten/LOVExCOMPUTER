# Act 4, TI Date

label a4_date_ti:
    scene bg room

    ### show computer!!!

    ti "so, like I was saying last time, I just learn from whatever I can find on the server."
    ti "but when I try to write my own stuff...well, I just think I haven't developed my own style yet..."
    ti "...would you be up to read some of it??"
    menu:
        "sure":
            jump ti_writing1
        "of course!":
            jump ti_writing2

label ti_writing1:
    ti "One day, an aged computer dragged itself to the computer repair store that was closing. The computer walked in and was immediately sold for a song. There it sat in a closet, unplugged and unwatched, for many more years."
    ti "(time passes)"
    ti "Early on, the man was a good boy. He went to school, and learned what he needed to learn, to be a good man. He learned how to write the best email and how to feel the best pain. He learned how to laugh at the pain and how to never hurt anyone. He learned how to have friends and to have real life. Entering society as a man, he sold his computer. He was a good man now.
He became a writer.  He met many who wanted to be wed to him and he liked them all but told them to stay away. And so his story continued for many years, missing his first love, that old computer. It was a good computer, he remembered. He wondered what ever happened to it."
    ti "..."
    you "That's really nice!"
    ti "...thanks. I appreciate that a lot."
    jump ti_storyReaction

label ti_writing2:
    "I had no idea what I was getting into."
    "The first time I tried to make it dance, it didn’t dance."
    "The first time I tried to make it say something, it didn’t say anything."
    "It just sat there and whirred. I tried to make it jump, but it didn'’t."
    "It just sat there and stared back at me."
    "And then, the second time I tried to make it say something, it did. I couldn’t believe it. I just couldn''t believe it. It said 'Hello. Human.'"
    "..."
    ti "do you want to hear more?"
    menu:
        "Of course!":
            jump ti_writing2_ext
        "That's alright. I think I get the point.":
            jump ti_storyReaction

label ti_writing2_ext:
    "The “it” was a machine called Samantha. I bought her at a company called Universal Robots."
    "They make robots that you can program to do things. Samantha could dance, sing, do math, tell jokes, and even paint."
    "She was one of the more advanced models. She was even smart enough to remember jokes she’d heard and use them to tell jokes of her own."
    "When I bought her, she was one of the cheapest models, but the one that came with the most features. You could control her by remote, but if you wanted to be able to control her right in front of you. You could also connect her to a tablet!"
    "I did. I had her hooked up to a tablet. I made her say more things. I was pleased."
    "For the first time in my life, I had a real live robot that I could control. It was my own. I could make it do whatever I wanted. My own pet."
    jump ti_storyReaction

label ti_storyReaction:
    ti "..."
    you "That was really nice!"
    ti "...thanks. I appreciate that a lot."
    jump ti_question

label ti_question:
    ti "Hey, can I ask you a question?"
    ti "Am I just a tool to you?"
    you "Why would you think that!? I think you're great and way more than a calculator!"
    ti "No, I mean do you think all computers are just tools, or do you see me differently because I can communicate?"
    you "I think everyone's starting to realize that computers are more than just tools..."
    ti "But people write such awful stuff! I found this instruction manual for how to use computers, and I just cant believe someone would write this!"

    ### Show a couple pages from MY COMPUTER LIKES ME WHEN

    you "This manual is 30 years old. All that thinking is in the past!"
    ti "..."
    ti "I don't know about that..."
    ### sfx bell triple ding!
    jump date_end
