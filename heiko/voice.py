import random
import os
from watson_developer_cloud import TextToSpeechV1
import pygame


def say(cfgobj, what, user=None):

    # if sound is disabled, do nothing
    if cfgobj["voice"]["enable"] is False:
        return

    try:
        pygame.mixer.init()

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
            pygame.mixer.music.load("{}{}.ogg".format(cfgobj["voice"]["path_user_greetings"], user))

        pygame.mixer.music.play()

    except Exception:
        pass


def generate_mp3(cfgobj, text, outfile):
    """
    Generate voice files
    """

    text_to_speech = TextToSpeechV1(
        iam_apikey=cfgobj["voice"]["watson_api_key"],
        url=cfgobj["voice"]["watson_endpoint"]
    )

    with open(outfile, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                'audio/ogg;codecs=vorbis',
                'en-US_MichaelVoice'
            ).get_result().content)


def greet_user(cfgobj, user):
    """
    Play individual greeting for user and generate
    if it does not exist.
    """

    # if sound is disabled, do nothing
    if cfgobj["voice"]["enable"] is False:
        return

    # generate sound if not existed
    p = os.path.expanduser("%s/%s.ogg" % (cfgobj["voice"]["path_user_greetings"], user))
    if not os.path.isfile(p):
        generate_mp3(cfgobj, "Hello %s!" % user, p)

    # play sound
    say(cfgobj, "user", user)
