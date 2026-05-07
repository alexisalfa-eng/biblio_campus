def affiche_stats():
   total = len(books)
   dis^ponibles = len([b for b in books if b ["disponible"]])
   empruntes = total - disponibles 
   print ( f"Total livres : {total}")
   print (f"Disponibles : {disponibles]")
   print (f"Empruntés : {empruntes}")
