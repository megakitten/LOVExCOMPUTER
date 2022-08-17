### Not Referenced in v1.0 ###
# Act 5, Mac Date

label date_mac: ## switch with date_mac in v2

    scene mal 00 with Dissolve(1)
    play music "audio/DateNight.mp3"
    show macFront


    mac "Hiii!"

    ### flash computer blush image? or pinkish diamond ai image ###
    menu:
        "uh...":
            jump mac_invitation
        "...":
            jump mac_invitation

label mac_invitation:
    mac "Do you want to look at some art?"
    menu:
        "Yeah of course!":
            jump mac_clipArtGallery
        "uh...I'll be *right* back":
            jump mac_leave

label mac_clipArtGallery:

    ### somehow show user a bunch of clip art ###

label mac_leave:
    menu:
        "Nevermind! Let's look at some art!":
            jump mac_next
        "just a sec...":
            jump a2_reset_choice

label mac_moreInfo:

    ### add content here if time

    you "how often do you feel that way?"
    mac "oh! well like...all the time, really!"
    jump mac_next


label mac_next:
    ###

    ### bring up


    ## PERSONALITY ETC ##
    # Mac is creative, innovative, and individualistic
    # but also a bit nervous and emotionally fragile.
    # They are into art and they have a passion for helping others.
    # G3 is (possibly) an Aquarius. Their favorite activities are all
    # art-related, and they are always looking for ways
    # to improve the world around them.
    # They can be overly idealistic
    # and they can become detached from reality at times.
    # They like to read old design books on things like color theory.
    # Their favorite color is light blue, and their favorite food is salmon.
