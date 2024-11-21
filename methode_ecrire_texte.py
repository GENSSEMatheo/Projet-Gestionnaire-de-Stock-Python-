import pygame 

def ecrire_texte(support,texte,x,y,taille,couleur,police):
        police_et_taille = pygame.font.Font(police, taille)
        texte = police_et_taille.render(texte, True, couleur)
        position = texte.get_rect(center=(x,y))
        support.blit(texte, position)