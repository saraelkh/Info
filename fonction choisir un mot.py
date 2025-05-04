def choisir_mot():
    with open("mots.txt", encoding="utf-8") as fichier:
        mots = [ligne.strip().lower() for ligne in fichier if ligne.strip()]
    return random.choice(mots)