import spacy
from spacy.tokens import DocBin
import json
from numpy import random
#transformation en donnee binaire

nlp = spacy.blank("fr") # On crée un modèle vide en français
db_train = DocBin()

# Charge tes données annotées (exemple)
with open('annotations.json', 'r') as f:
    data = json.load(f)
annotations = data['annotations']
random.seed(42) 
random.shuffle(annotations)

# 3. C'EST ICI QUE LE CODE COUPE TON DATASET EN DEUX AUTOMATIQUEMENT
split_index = int(len(annotations) * 0.8)  # Trouve l'endroit où couper à 80%
train_data = annotations[:split_index]      # Prend les premiers 80% pour l'entraînement
valid_data = annotations[split_index:]      # Prend les 20% restants pour la validation


for text, annot in train_data:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            ents.append(span)
    doc.ents = ents
    db_train.add(doc)

db_train.to_disk("./train.spacy") 
# python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./valid.spacy  pour l'entrainement

db_valid = DocBin()
for text, annot in valid_data:  # On utilise uniquement les données de validation !
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            ents.append(span)
    doc.ents = ents
    db_valid.add(doc)

db_valid.to_disk("./valid.spacy")