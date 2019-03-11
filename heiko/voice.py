import pygame

def say(what):

    try:
        pygame.mixer.init()

        if what == "welcome":
            pygame.mixer.music.load("./heiko/sound/welcome.mp3")
        elif what == "error":
            pygame.mixer.music.load("./heiko/sound/error.mp3")
        elif what == "cheers":
            pygame.mixer.music.load("./heiko/sound/cheers.mp3")
        elif what == "quit":
            pygame.mixer.music.load("./heiko/sound/quit.mp3")
        elif what == "transaction_successful":
            pygame.mixer.music.load("./heiko/sound/transaction_successful.mp3")

        pygame.mixer.music.play()
    except:
        pass
