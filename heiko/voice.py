import os
from heiko.utils import log
from watson_developer_cloud import TextToSpeechV1
import pygame

def say(cfgobj, what, user=None):

    try:
        pygame.mixer.init()

        if what == "welcome":
            pygame.mixer.music.load(cfgobj["voice"]["path_sounds"] + "/welcome.wav")
        elif what == "error":
            pygame.mixer.music.load(cfgobj["voice"]["path_sounds"] + "/error.wav")
        elif what == "cheers":
            pygame.mixer.music.load(cfgobj["voice"]["path_sounds"] + "/cheers.wav")
        elif what == "quit":
            pygame.mixer.music.load(cfgobj["voice"]["path_sounds"] + "/quit.wav")
        elif what == "transaction_successful":
            pygame.mixer.music.load(cfgobj["voice"]["path_sounds"] + "/transaction_successful.wav")
        elif what == "user":
            pygame.mixer.music.load(cfgobj["voice"]["path_user_greetings"] + "/%s.ogg" % user )

        pygame.mixer.music.play()

    except Exception as e:
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

