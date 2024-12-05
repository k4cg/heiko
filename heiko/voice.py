import os
import time
import pygame
import pyttsx3


def say(cfgobj, what, user=None):

    # if sound is disabled, do nothing
    if cfgobj["voice"]["enable"] is False:
        return

    try:
        pygame.mixer.init(buffer=4096, frequency=22050)

        if what == "welcome":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["welcome"])
        elif what == "error":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["error"])
        elif what == "cheers":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["cheers"])
        elif what == "admin":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["admin"])
        elif what == "quit":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["quit"])
        elif what == "transaction_success":
            pygame.mixer.music.load(cfgobj["voice"]["sounds"]["transaction_success"])
        elif what == "user":
            pygame.mixer.music.load(os.path.join(cfgobj["voice"]["path_user_greetings"], f"{user}.mp3"))

        pygame.mixer.music.play()

    except Exception:
        pass


def generate_mp3(text, outfile):
    """
    Generate voice files
    """

    engine = pyttsx3.init()
    engine.setProperty("voice", "english-us")
    engine.setProperty("rate", 160)
    engine.save_to_file(text, outfile)
    engine.runAndWait()
    while engine.isBusy():
        time.sleep(0.001)


def greet_user(cfgobj, user):
    """
    Play individual greeting for user and generate
    if it does not exist.
    """

    # if sound is disabled, do nothing
    if cfgobj["voice"]["enable"] is False:
        return

    # generate sound if not existed
    p = os.path.expanduser("%s/%s.mp3" % (cfgobj["voice"]["path_user_greetings"], user))
    if not os.path.isfile(p):
        generate_mp3("Hello %s!" % user, p)

    # play sound
    say(cfgobj, "user", user)
