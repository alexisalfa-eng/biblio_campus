def empruter_livre(livre):
    if livre["disponible"]:
       livre["disponible"] = False
       retur True
     return False


def rendre_livre(livre):
    livre["disponible"] = True
