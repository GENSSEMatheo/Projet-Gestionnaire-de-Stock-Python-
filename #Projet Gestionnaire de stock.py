#Projet Gestionnaire de stocke 
#---------------------------------------------------------------------------------
import pygame
import json
import os
import time
from methodes_tri import*
from methode_input_tkinter import*
from methode_dessiner_bouton import*
from methode_ecrire_texte import*
from dictionnaire_boutons import*
from methode_modif_commandes import*
from methode_son import*
#---------------------------------------------------------------------------------
#----------------------------------
#Fenêtre Pygame - ACCUEIL 
#----------------------------------

class FenetreAccueil:                                                                                                                                   
    def __init__(self):                                                                                                                                 
        self.titre = "Gestionnaire de stock - ACCUEIL"                                                                               
        self.largeur = 800                                                                                                                              
        self.hauteur = 400                                                                                                                              
        self.favicon = pygame.image.load("Images Icones/Logo Favicon.png")                                                                              
        self.fond_ecran = pygame.image.load("Fond écran accueil.jpg")                                                                                   
        self.icone = pygame.image.load("Images Icones/Logo App.png")                                                                                    
        self.icone_hover = pygame.transform.scale(pygame.image.load("Images Icones/Logo App NB.png"), (200, 200))                                       
        self.fenetre=None                                                                                                                               

    def initialiser(self):                                                                                                                              
        pygame.init()   
        jouer_son("Présentation.mp3")                                                                                                                             
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))                                                                            
        pygame.display.set_caption(self.titre)                                                                                                          
        pygame.display.set_icon(self.favicon)                                                                                                           
        self.fenetre.blit(self.fond_ecran, (0, 0))                                                                                                      

    def afficher_contenu(self):                                                                                                              
        if self.clic_sur_icone(pygame.mouse.get_pos()):                                                                                                 
            self.fenetre.blit(pygame.transform.scale(self.icone_hover, (200, 200)), (self.largeur // 2 - 100, self.hauteur // 2 - 100))
        else:                                                                                                                                           
            self.fenetre.blit(pygame.transform.scale(self.icone, (200, 200)), (self.largeur // 2 - 100, self.hauteur // 2 - 100))                                                                                        
        ecrire_texte(self.fenetre,"Cliquez pour continuer",self.largeur // 2, self.hauteur // 2 - 100 + 220,25,(255, 255, 255),"PlayfairDisplay-Italic-VariableFont_wght.ttf")

    def gerer_evenements(self):                                                                                                                         
        for event in pygame.event.get():                                                                                                                
            if event.type == pygame.QUIT:                                                                                                               
                pygame.quit()                                                                                                                           
            elif event.type == pygame.MOUSEBUTTONDOWN:                                                                                                  
                x,y = event.pos
                if (self.largeur // 2 - 100 <= x <= self.largeur // 2 - 100 + 200) and (self.hauteur // 2 - 100 <= y <= self.hauteur // 2 - 100 + 200): 
                    self.ouvrir_fenetre_application()                                                                                                   
        return True

    def clic_sur_icone(self, position):                                                                                                                 
        icone_rect = pygame.Rect(self.largeur // 2 - 100, self.hauteur // 2 - 100, 200, 200)                                                            
        return icone_rect.collidepoint(position)                                                                                                        

    def ouvrir_fenetre_application(self):                                                                                                               
        pygame.quit()                                                                                                                                  
        time.sleep(0.1)                                                                                                                                 
        fenetre_application = FenetreApplication(self.fond_ecran)                                                                                       
        fenetre_application.initialiser()                                                                                                               
        fenetre_application.boucle_principale()                                                                                                         
        continuer=False

#----------------------------------                                         
#Fenêtre Pygame - APPLICATION                                           
#----------------------------------                                         

class FenetreApplication:                                                                                                                              
    def __init__(self, fond_ecran):                                                                                                                    
        self.titre = "Gestionnaire de stock - APPLICATION"                                                                          
        self.largeur = 1200                                                                                                                            
        self.hauteur = 750                                                                                                                             
        self.icone = pygame.image.load("Images Icones/Logo App.png")                                                                                   
        self.fond_ecran = fond_ecran                                                                                                                   
        self.fenetre = None                                                                                                                            
        self.stocks = []
        self.stocks_original = []
        self.donnees_livraisons = []
        self.logo_alpha = pygame.image.load("Images Icones/Ordre alphabétique.png")
        self.logo_rupture = pygame.image.load("Images Icones/Rupture de stock.png")
        self.logo_stock = pygame.image.load("Images Icones/Logo en stock.png")
        self.tableau_couleur = (255, 255, 255)
        self.texte_couleur = (0, 0, 0)
        self.ligne_couleur = (0, 0, 0)
        self.est_triee = False
        self.trie_rupture = False
        self.trie_stock = False
        self.charger_stocks()
        self.sauvegarder_stocks()
        

    def initialiser(self):                                                                                                                            
        pygame.init()                                                                                                                                   
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))                                                                                                
        pygame.display.set_caption(self.titre)                                                                                                          
        pygame.display.set_icon(self.icone)                                                                                                             
        self.fenetre.blit(self.fond_ecran, (0, 0)) 
        pygame.draw.rect(self.fenetre, (0, 102, 204), pygame.Rect(0, 0, 1200, 50)) 
        pygame.draw.rect(self.fenetre, (0, 102, 204), pygame.Rect(740, 50, 60, self.hauteur - 50))
        self.fenetre.blit(pygame.transform.scale(self.logo_alpha, (35, 35)), (753, 130))
        self.fenetre.blit(pygame.transform.scale(self.logo_rupture, (50, 50)), (745, 360))
        self.fenetre.blit(pygame.transform.scale(self.logo_stock, (50, 50)), (745, 590))
        pygame.draw.rect(self.fenetre, (0, 0, 0), pygame.Rect(650, 50, 90, self.hauteur - 50))
        pygame.draw.rect(self.fenetre, (0, 0, 0), pygame.Rect(0, 50, 650, 40))
        ecrire_texte(self.fenetre,"C  O  M  M  A  N  D  E  S        F  O  U  R  N  I  S  S  E  U  R  S",650 // 2, 12 + 15 + 45,30,(255, 255, 255),None)
        self.sauvegarder_stocks()
        
    def afficher_contenu(self):
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(0, 90, 650, self.hauteur - 50))
        self.dessiner_tableau_stocks()

        for bouton in boutons_parametres:
            dessiner_bouton(self.fenetre, bouton["x"], bouton["y"], bouton["largeur"], bouton["hauteur"], bouton["couleur"], bouton["texte"], (0, 0, 0))
            
        x, y = pygame.mouse.get_pos()
        for bouton in boutons_parametres:
            if bouton["x"] <= x <= bouton["x"] + bouton["largeur"] and bouton["y"] <= y <= bouton["y"] + bouton["hauteur"]:
                couleur_survol = []
                for c in bouton["couleur"]:
                    if c + 100 <= 255:
                        couleur_survol.append(c + 100)
                    else:
                        couleur_survol.append(c)
                            
                dessiner_bouton(self.fenetre, bouton["x"], bouton["y"], bouton["largeur"], bouton["hauteur"], couleur_survol, bouton["texte"], (0, 0, 0))

        self.tableau_fournisseur()
        self.sauvegarder_stocks()

    def boucle_principale(self):    
        self.afficher_contenu()
        continuer = True                                                                                                                              
        while continuer:                                                                                                                                
            for event in pygame.event.get():                                                                                                            
                if event.type == pygame.QUIT:                                                                                                           
                    continuer = False                                                                                                              
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if (952 <= x <= 1052) and (12 <= y <= 42): 
                        jouer_son("Vider stock.mp3")
                        print("Vous avez cliquez sur VIDER LES STOCKS")
                        time.sleep(2)
                        self.stocks=[]
                        self.sauvegarder_stocks()
                    elif (822 <= x <= 922) and (12 <= y <= 42):
                        jouer_son("Ajouter.mp3")
                        print("Vous avez cliquez sur AJOUTER")
                        time.sleep(2)
                        self.ajout()
                    elif (1082 <= x <= 1182) and (12 <= y <= 42):
                        jouer_son("Sup quantité.mp3")
                        print("Vous avez cliquez sur SUPPRIMER UNE QUANTITE")
                        time.sleep(2)
                        self.retirer_une_quantite()
                    elif (745 <= x <= 795) and (360 <= y <= 410):
                        print("Vous avez cliquez sur FILTRER PAR RUPTURES DE STOCK")
                        self.rupture_de_stock_trie()
                    elif (753 <= x <= 788) and (130 <= y <= 165):
                        if self.est_triee == False:
                            jouer_son("Tri croissant.mp3")
                            print("Vous avez fait un TRI PAR ORDRE CROISSANT DES LETTRES DE L'ALPHABET")
                            trier_ordre_alpha(self.stocks)
                            self.est_triee = True
                        else:
                            jouer_son("Tri decroissant.mp3")
                            print("Vous avez fait un TRI PAR ORDRE DECROISSANT DES LETTRES DE L'ALPHABET")
                            triee_decr_alpha(self.stocks)
                            self.est_triee = False
                    elif (745 <= x <= 795) and (590 <= y <= 640):
                        print("Vous avez cliquez sur FILTRER PAR PRODUITS EN STOCK")
                        self.en_stock_trie()
                    elif (20 <= x <= 220) and (12 <= y <= 42):
                        jouer_son("Ajout commande.mp3")
                        print("Vous avez cliquez sur AJOUTER UNE COMMANDE")
                        time.sleep(2)
                        self.ajout_commande()
                    elif (240 <= x <= 340) and (12 <= y <= 42):
                        jouer_son("Modifier commande.mp3")
                        print("Vous avez cliquez sur MODIFIER UNE COMMANDE")
                        time.sleep(2)
                        self.modifier()
                    elif (360 <= x <= 460) and (12 <= y <= 42):
                        jouer_son("Supprimer commande.mp3")
                        print("Vous avez cliquez sur SUPPRIMER UNE COMMANDE")
                        time.sleep(2)
                        self.supprimer_ligne_commande()
                    elif (480 <= x <= 680) and (12 <= y <= 42):
                        jouer_son("Livrer commande.mp3")
                        print("Vous avez cliquez sur LIVRER UNE COMMANDE")
                        time.sleep(2)
                        self.livre_la_commande()
     
            self.afficher_contenu()                                                                                                                    
            pygame.display.flip()                                                                                                                       
        self.sauvegarder_stocks()                                               
                            
    def charger_stocks(self):
        if os.path.exists("Stocks.json"):
            with open("Stocks.json", "r") as f:
                self.stocks = json.load(f)

    def sauvegarder_stocks(self):
        with open("Stocks.json", "w") as f:
            json.dump(self.stocks, f)

    def dessiner_tableau_stocks(self):               
        tableau_x = 800
        tableau_y = 50
        tableau_largeur = 400
        tableau_hauteur = self.hauteur - tableau_y
        pygame.draw.rect(self.fenetre, self.tableau_couleur, (tableau_x, tableau_y, tableau_largeur, tableau_hauteur))
        en_tetes = ["Nom", "État", "Quantité"]
        espace_entre_colonnes = tableau_largeur // len(en_tetes)
        for i in range(len(en_tetes)):
            en_tete = en_tetes[i]
            ecrire_texte(self.fenetre,en_tete,tableau_x + (i + 0.5) * espace_entre_colonnes,tableau_y + 20,25,self.texte_couleur,None)
        for i in range(1, len(self.stocks) + 1):
            if 800 <= pygame.mouse.get_pos()[0] <= 1200 and (50 + i * 30) <= pygame.mouse.get_pos()[1] <= (50 + (i + 1) * 30):
                pygame.draw.rect(self.fenetre, (220,220,220), pygame.Rect(800, 50 + i * 30, 400, 30))
            else:
                pygame.draw.line(self.fenetre, self.ligne_couleur,
                                (tableau_x, tableau_y + i * 30),
                                (tableau_x + tableau_largeur, tableau_y + i * 30))
        for i in range(len(en_tetes) + 1):
            pygame.draw.line(self.fenetre, self.ligne_couleur,
                             (tableau_x + i * espace_entre_colonnes, tableau_y),
                             (tableau_x + i * espace_entre_colonnes, tableau_y + tableau_hauteur))
    
        for i in range(len(self.stocks) + 2):
            pygame.draw.line(self.fenetre, self.ligne_couleur,
                             (tableau_x, tableau_y + i * 30),
                             (tableau_x + tableau_largeur, tableau_y + i * 30))

        ligne_y = tableau_y + 50
        for stock in self.stocks:
            ligne_x = tableau_x
            etat = stock["etat"]
            couleur_texte = self.texte_couleur
            
            if etat in ["En rupture", "rupture", "en rupture", "EN RUPTURE", "Rupture", "RUPTURE"]:
                couleur_texte = (255, 0, 0)

            for info in ["nom", "etat", "quantite"]:
                ecrire_texte(self.fenetre,str(stock[info]),ligne_x + espace_entre_colonnes // 2, ligne_y - 5.5,20,couleur_texte,None)
                ligne_x += espace_entre_colonnes
            ligne_y += 30
        self.sauvegarder_stocks()
   
    def ajout(self):
        quantite=None
        jouer_son("Porte qui grince.mp3")
        produit = str(input_tkinter("Entrez le\nNOM DU PRODUIT\nque vous souhaitez ajouter à votre stock : "))
        if produit in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
            jouer_son("Opération annuler.mp3")
            print("L'opération à été annuler")
            return self.afficher_contenu
        jouer_son("Porte qui grince.mp3")
        etat = str(input_tkinter("Entrez l'état :\n(Stock/Rupture)\ndu produit\n"+ produit +"\nque vous souhaitez ajouter à votre stock : "))
        if etat in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
            jouer_son("Opération annuler.mp3")
            print("L'opération à été annuler")
            return self.afficher_contenu
        
        if etat in ["En rupture", "rupture", "en rupture", "EN RUPTURE", "Rupture", "RUPTURE"]:
            etat="En rupture"
            quantite=0
         
        else : 
            etat = "En stock"
            jouer_son("Porte qui grince.mp3")
            quantite = int(input_tkinter("Entrez la\nQUANTITE\nque vous posséderez dès à présent du produit\n"+ produit +"\nque vous souhaitez ajouter à votre stock : "))
            if quantite in ["STOP", "STOP", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
                jouer_son("Opération annuler.mp3")
                print("L'opération à été annuler")
                return self.afficher_contenu
        
        for i in self.stocks:
            if i["nom"] == produit:
                i["quantite"] += quantite
                if i["quantite"] > 0 :
                    i["etat"] = "En stock"
                if i["quantite"] == 0 :
                    i["etat"] = "En rupture"
                break
        
        else:
            self.stocks.append({"nom": produit, "etat": etat, "quantite": quantite})
        
        self.sauvegarder_stocks()
        self.afficher_contenu()
        
        pygame.display.flip()

        recommencer = str(input_tkinter("Voulez vous ajouter de nouveau un produit en plus de" + produit +"\nOUI ou NON : "))
        if recommencer in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
            self.ajout()
        else:
            return self.afficher_contenu()
                
    def retirer_une_quantite(self):
        jouer_son("Porte qui grince.mp3")
        prod_quantite_a_retirer = str(input_tkinter("De quel\nPRODUIT\nsouhaitez vous retirez une quantité : "))
        produit_trouve = False
        for l in self.stocks:
            if l["nom"] == prod_quantite_a_retirer :
                produit_trouve = True
                jouer_son("Porte qui grince.mp3")
                quantite_a_retirer = int(input_tkinter("Quelle\nQUANTITE\nsouhaitez vous retirer à " + prod_quantite_a_retirer + " : "))
                while quantite_a_retirer > l["quantite"]:
                    print("Vous ne pouvez pas retirer une quantité supérieure à celle déjà existante, veuillez donner une quantité valable et inférieure à", l["quantite"])
                    jouer_son("Porte qui grince.mp3")
                    quantite_a_retirer = int(input_tkinter("Quelle\nQUANTITE\nsouhaitez vous retirer à " + prod_quantite_a_retirer + " : "))
                l["quantite"] -= quantite_a_retirer
        if not produit_trouve:
            print("Aucun produit n'existe au nom de",prod_quantite_a_retirer)
        self.sauvegarder_stocks()
        self.afficher_contenu()

        pygame.display.flip()

    def rupture_de_stock_trie(self):
        if self.trie_rupture == False: 
            jouer_son("Filtrer rupture.mp3")
            self.stocks_original = self.stocks.copy()
            stocks_en_rupture = [stock for stock in self.stocks if stock["etat"] in ["En rupture", "en rupture", "Rupture", "rupture"]]
            self.stocks = stocks_en_rupture
        else: 
            jouer_son("Filtrer rupture non.mp3")
            self.stocks = self.stocks_original.copy()
        self.afficher_contenu()
        self.trie_rupture = not self.trie_rupture

    def en_stock_trie(self):
        if self.trie_stock == False: 
            jouer_son("Filtrer stock.mp3")
            self.stocks_original = self.stocks.copy()
            stocks_en_stock = [stock for stock in self.stocks if stock["etat"] not in ["En rupture", "en rupture", "Rupture", "rupture"]]
            self.stocks = stocks_en_stock
        else: 
            jouer_son("Filtrer stock non.mp3")
            self.stocks = self.stocks_original.copy()
        self.afficher_contenu()
        self.trie_stock = not self.trie_stock

    def sauvegarder_donnees_livraisons(self):
        with open("Livraisons fournisseurs.json", "w") as f:
            json.dump(self.donnees_livraisons, f)

    def charger_donnees_json_livraisons(self):  
        if os.path.exists("Livraisons fournisseurs.json"):
            with open("Livraisons fournisseurs.json", "r") as f:
                self.donnees_livraisons = json.load(f)

    def tableau_fournisseur(self):
        self.charger_donnees_json_livraisons()
        colonnes = ["Nom du fournisseur", "Produit à livrer", "Quantité", "Produits livrés"]
        colonne_largeur = 150  
        colonne_hauteur = 30  
        tableau_x = 0 
        tableau_y = 90
        tableau_largeur = 650  
        tableau_hauteur = 660  
        for i in range(1, len(self.donnees_livraisons) + 1):
            if tableau_x <= pygame.mouse.get_pos()[0] <= tableau_x + tableau_largeur and (tableau_y + i * colonne_hauteur) <= pygame.mouse.get_pos()[1] <= (tableau_y + (i + 1) * colonne_hauteur):
                pygame.draw.rect(self.fenetre, (220, 220, 220), pygame.Rect(tableau_x, tableau_y + i * colonne_hauteur, tableau_largeur, colonne_hauteur))
            else:
                pygame.draw.line(self.fenetre, (0, 0, 0), (tableau_x, tableau_y + i * colonne_hauteur), (tableau_x + tableau_largeur, tableau_y + i * colonne_hauteur))

        for i in range(len(self.donnees_livraisons) + 2):
            pygame.draw.line(self.fenetre, (0, 0, 0), (tableau_x, tableau_y + i * colonne_hauteur), (tableau_x + tableau_largeur, tableau_y + i * colonne_hauteur))

        colonne_x = tableau_x
        for colonne in colonnes:
            ecrire_texte(self.fenetre,colonne,colonne_x + colonne_largeur // 2,tableau_y + colonne_hauteur // 2,22,(0, 0, 0),None)
            pygame.draw.line(self.fenetre, (0, 0, 0), (colonne_x, tableau_y), (colonne_x, tableau_y + tableau_hauteur))
            colonne_x += colonne_largeur

        pygame.draw.line(self.fenetre, (0, 0, 0), (tableau_x, tableau_y + tableau_hauteur), (tableau_x + tableau_largeur, tableau_y + tableau_hauteur))

        ligne_y = tableau_y + 30
        for donnees_fournisseurs in self.donnees_livraisons:
            ligne_x = tableau_x
            for infos in ["nom du fournisseur", "produit a livrer", "quantite", "produit livre"]:
                ecrire_texte(self.fenetre,str(donnees_fournisseurs[infos]),ligne_x + colonne_largeur // 2,ligne_y + colonne_hauteur // 2,20,self.texte_couleur,None)
                ligne_x += colonne_largeur
            ligne_y += colonne_hauteur

    def ajout_commande(self):
        jouer_son("Porte qui grince.mp3")
        fournisseur = input_tkinter("Quel est le nom du\nFOURNISSEUR\nde votre commande ? : ")
        if fournisseur in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
                jouer_son("Opération annuler.mp3")
                print("L'opération à été annuler")
                return self.afficher_contenu
        jouer_son("Porte qui grince.mp3")
        produit_a_livrer = input_tkinter("Quel est le\nNOM DU PRODUIT\nque"+ fournisseur +"va vous livrer ? : ")
        if produit_a_livrer in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
                jouer_son("Opération annuler.mp3")
                print("L'opération à été annuler")
                return self.afficher_contenu
        jouer_son("Porte qui grince.mp3")
        quantite_a_livrer = input_tkinter("Quellle\nQUANTITE\navez vous à livrer pour" + produit_a_livrer +"livré par" + fournisseur + " ? : ")
        if quantite_a_livrer in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
                jouer_son("Opération annuler.mp3")
                print("L'opération à été annuler")
                return self.afficher_contenu

        for donnees in self.donnees_livraisons:
            if produit_a_livrer == donnees["produit a livrer"]:
                quantite_a_livrer += self.donnees_livraisons["quantite"]
                
        self.donnees_livraisons.append({"nom du fournisseur": fournisseur, "produit a livrer": produit_a_livrer, "quantite": quantite_a_livrer, "produit livre": "Non"})
        jouer_son("Porte qui grince.mp3")
        autre_cmd = str(input_tkinter("Avez-vous une\nAUTRE COMMANDE\nà entrer en plus de" + produit_a_livrer +" ? : "))
        if autre_cmd in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
            self.ajout_commande()
        else :
            self.sauvegarder_donnees_livraisons()
            self.afficher_contenu()
            print("Fin de l'opération")

    def modifier(self):
        jouer_son("Porte qui grince.mp3")
        quoi_modif = str(input_tkinter("Que souhaitez vous\nMODIFIER\nparmis\nNom du fournisseur/Produit à livrer/Quantité\n? : "))
        if quoi_modif in ["STOP", "stop", "annule", "ANNULE", "annuler", "ANNULER", "Annuler"]:
                jouer_son("Opération annuler.mp3")
                print("L'opération à été annuler")
                return self.afficher_contenu

        if quoi_modif in ["Nom du fournisseur","nom du fournisseur","NOM DU FOURNISSEUR","fournisseur","Fournisseur","FOURNISSEUR"]:
            modif_fournisseur(self.donnees_livraisons)
            jouer_son("Porte qui grince.mp3")
            autre = str(input_tkinter("Souhaitez vous \nMODIFIER LE NOM D'UN AUTRE FOURNISSEUR\nOUI ou NON ? : "))
            self.sauvegarder_donnees_livraisons()
            if autre in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
                modif_fournisseur(self.donnees_livraisons)
            else:
                self.afficher_contenu()
                print("Fin de l'opération")

        if quoi_modif in ["Produit à livrer","Produit","PRODUIT", "PRODUIT A LIVRER","produit à livrer"]:
            modif_produit_a_livre(self.donnees_livraisons)
            jouer_son("Porte qui grince.mp3")
            autre = str(input_tkinter("Souhaitez vous \nMODIFIER LE NOM D'UN AUTRE PRODUIT\nOUI ou NON ? : "))
            self.sauvegarder_donnees_livraisons()
            if autre in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
                modif_produit_a_livre(self.donnees_livraisons)
            else:
                self.afficher_contenu()
                print("Fin de l'opération")

        if quoi_modif in ["quantite","QUANTITE","Quantité", "quantité"]:
            modif_quantite_a_livre(self.donnees_livraisons)
            jouer_son("Porte qui grince.mp3")
            autre = str(input_tkinter("Souhaitez vous \nMODIFIER UNE AUTRE QUANTITE\nOUI ou NON ? : "))
            self.sauvegarder_donnees_livraisons()
            if autre in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
                modif_quantite_a_livre(self.donnees_livraisons)
            else:
                self.afficher_contenu()
                print("Fin de l'opération")
        jouer_son("Porte qui grince.mp3")
        autre_modif = str(input_tkinter("Souhaitez vous effectué\nUNE AUTRE MODIFICATION\nOUI ou NON ? : "))
        if autre_modif in ["oui","OUI","Oui","Yes","ui","UI","O","o","Y","yes","YES"]:
            self.modifier()
        else:
            self.afficher_contenu()
            print("Fin de l'opération de modification")

    def supprimer_ligne_commande(self):
        jouer_son("Porte qui grince.mp3")
        ligne_a_supp = int(input_tkinter("Veuillez entrer le \nNUMERO DE LA LIGNE QUE VOUS SOUHAITEZ RETIRER\nparmis celles issue du tableau :"))
        if 0 < ligne_a_supp <= len(self.donnees_livraisons) +1 :
            self.donnees_livraisons.pop(ligne_a_supp - 1)
            self.sauvegarder_donnees_livraisons()
            print("Modification effectuée avec succès !")
            self.afficher_contenu()
        else:
            print("Numéro de ligne invalide.")

    def livre_la_commande(self):
        dico_non_livree = []
        for commande in self.donnees_livraisons:
            if commande["produit livre"] == "Non":
                dico_non_livree.append(commande)

        jouer_son("Porte qui grince.mp3")
        quoi_livrer = int(input_tkinter("Veuillez entrer le \nNUMERO DE LA LIGNE DE LA COMMANDE QUE VOUS SOUHAITEZ LIVRER : "))
        if 0 < quoi_livrer <= len(dico_non_livree):
            produit = dico_non_livree[quoi_livrer - 1]["produit a livrer"]
            etat = "En stock"
            quantite = int(dico_non_livree[quoi_livrer - 1]["quantite"])
            produit_trouve = False
            for i in self.stocks:
                if i["nom"] == produit:
                    i["quantite"] += quantite
                    if i["quantite"] > 0:
                        i["etat"] = "En stock"
                    if i["quantite"] == 0:
                        i["etat"] = "En rupture"
                    produit_trouve = True
                    break
            if not produit_trouve:
                self.stocks.append({"nom": produit, "etat": etat, "quantite": quantite}) 

            for commande in self.donnees_livraisons:
                if commande == dico_non_livree[quoi_livrer - 1]:
                    commande["produit livre"] = "Oui"
            
            self.sauvegarder_donnees_livraisons()
            self.sauvegarder_stocks()
            self.afficher_contenu()
            print("La commande a été livrée avec succès")

            jouer_son("Porte qui grince.mp3")
            autre_livraison = input_tkinter("Souhaitez vous\nLIVRER UNE AUTRE COMMANDE\nOUI ou NON ? : ")
            if autre_livraison in ["oui", "o", "yes", "y"]:
                self.livre_la_commande()
            else:
                self.afficher_contenu()
                print("Fin de l'opération de livraison")
        else:
            print("Numéro de ligne invalide.")


fenetre_accueil = FenetreAccueil()                                                                                                                      
fenetre_accueil.initialiser()                                                                                                                           
continuer = True                                                                                                                                        
while continuer:                                                                                                                                        
    continuer = fenetre_accueil.gerer_evenements()                                                                                                      
    fenetre_accueil.afficher_contenu()                                                                                                                  
    pygame.display.flip()                                                                                                                               
                                                        

