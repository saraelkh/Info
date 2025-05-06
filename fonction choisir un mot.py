def choisir_mot():
    fichier = open("mots.txt", encoding="utf-8")
    mots = []
    for ligne in fichier:
        ligne = ligne.strip()
        if ligne:
            mots.append(ligne.lower())
    fichier.close()
    return random.choice(mots)
