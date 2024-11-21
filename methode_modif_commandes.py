from methode_input_tkinter import*

def modif_fournisseur(dico):
    ligne = int(input_tkinter("Parmis les\nLIGNES DU TABLEAU\nlaquelle souhaitez vous\nMODIFIER\n ? :" ))
    if 0 < ligne <= len(dico) +1 :
        nouveau_nom = input_tkinter("Entrez le\nNOUVEAU NOM DU FOURNISSEUR\n de la \nLIGNE" + ligne + ": ")
        dico[ligne-1]["nom du fournisseur"] = nouveau_nom
        print("Modification effectuée avec succès !")
    else:
        print("Numéro de ligne invalide.")

def modif_produit_a_livre(dico):
    ligne = int(input_tkinter("Parmis les\nLIGNES DU TABLEAU\nlaquelle souhaitez vous\nMODIFIER\n ? :" ))
    if 0 < ligne <= len(dico) +1 :
        nouveau_nom = input_tkinter("Entrez le\nNOUVEAU NOM DU PRODUIT A LIVRER\n de la \nLIGNE" + ligne + ": ")
        dico[ligne-1]["produit a livrer"] = nouveau_nom
        print("Modification effectuée avec succès !")
    else:
        print("Numéro de ligne invalide.")

def modif_quantite_a_livre(dico):
    ligne = int(input_tkinter("Parmis les\nLIGNES DU TABLEAU\nlaquelle souhaitez vous\nMODIFIER\n ? :" ))
    if 0 < ligne <= len(dico) +1 :
        nouveau_nom = input_tkinter("Entrez la\nNOUVELLE QUANTITE A LIVRER\n de la \nLIGNE" + ligne + ": ")
        dico[ligne-1]["quantite"] = nouveau_nom
        print("Modification effectuée avec succès !")
    else:
        print("Numéro de ligne invalide.")