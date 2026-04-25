import spacy

# On charge ton modèle WeDream
nlp = spacy.load("./output/model-best")

# On lui donne une phrase complexe pour le tester
phrase = "Je possède un leadership naturel et je sais faire preuve d'empathie en gestion de projet."
phrase1 = " je possède l'esprit d'equipe "

doc = nlp(phrase)

# On extrait les variables
competences_trouvees = [ent.text for ent in doc.ents]

print(f"Soft Skills détectées : {competences_trouvees}")