import pygame

def jouer_son(nom_fichier):
    pygame.mixer.init()
    pygame.mixer.music.load(nom_fichier)
    pygame.mixer.music.play()