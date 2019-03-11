import pygame

def say(what):

    try:
        pygame.mixer.init()

        if what == "welcome":
            pygame.mixer.music.load("./heiko/sound/welcome.wav")
        elif what == "error":
            pygame.mixer.music.load("./heiko/sound/error.wav")
        elif what == "cheers":
            pygame.mixer.music.load("./heiko/sound/cheers.wav")
        elif what == "quit":
            pygame.mixer.music.load("./heiko/sound/quit.wav")
        elif what == "transaction_successful":
            pygame.mixer.music.load("./heiko/sound/transaction_successful.wav")

        pygame.mixer.music.play()
    except:
        pass
