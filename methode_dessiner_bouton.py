import pygame

def dessiner_bouton(support_fenetre,x, y, largeur, hauteur, couleur, texte,couleur_texte):
        pygame.draw.rect(support_fenetre, couleur, pygame.Rect(x, y, largeur, hauteur), 0)
        font = pygame.font.Font(None, 20)
        texte_surface = font.render(texte, True, couleur_texte)
        texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
        support_fenetre.blit(texte_surface, texte_rect)