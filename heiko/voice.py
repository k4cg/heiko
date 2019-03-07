import pygame

def say(what):

    pygame.mixer.init()

    if what == "welcome":
        pygame.mixer.music.load("./sound/welcome.mp3")
    elif what == "error":
        pygame.mixer.music.load("./sound/error.mp3")
    elif what == "cheers":
        pygame.mixer.music.load("./sound/cheers.mp3")
    elif what == "quit":
        pygame.mixer.music.load("./sound/quit.mp3")
    elif what == "transaction_successful":
        pygame.mixer.music.load("./sound/transaction_successful.mp3")

    try:
        pygame.mixer.music.play()
    except:
        pass
