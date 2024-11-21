def trier_ordre_alpha(liste_avec_dict_interne):
    for i in range(1, len(liste_avec_dict_interne)):
        cle = liste_avec_dict_interne[i]
        j = i-1
        while j >= 0 and cle["nom"] < liste_avec_dict_interne[j]["nom"]:
            liste_avec_dict_interne[j + 1] = liste_avec_dict_interne[j]
            j -= 1
        liste_avec_dict_interne[j + 1] = cle

def triee_decr_alpha(liste_avec_dict_interne):
        n = len(liste_avec_dict_interne)
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if liste_avec_dict_interne[j]["nom"] > liste_avec_dict_interne[max_index]["nom"]:
                    max_index = j
            if max_index != i:
                liste_avec_dict_interne[i], liste_avec_dict_interne[max_index] = liste_avec_dict_interne[max_index], liste_avec_dict_interne[i]