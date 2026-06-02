#  Module d'Extraction de Soft Skills (NLP)

> **Contribution personnelle** à un projet d'équipe de **CVthèque intelligente dédiée aux RH du Cameroun 🇨🇲**.
> Ce dépôt contient uniquement la brique NLP responsable de la détection automatique des compétences comportementales (*soft skills*) dans les CV et lettres de motivation.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![spaCy](https://img.shields.io/badge/spaCy-3.x-09a3d5.svg)
![NLP](https://img.shields.io/badge/Task-NER-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)



Contexte du projet

Ce travail s'inscrit dans un projet collectif de développement d'une CVthèque intelligente, pensée spécifiquement pour répondre aux **besoins des professionnels RH au Cameroun**.

### 🇨🇲 Le constat

À l'issue d'observations faites auprès de recruteurs camerounais, plusieurs difficultés récurrentes ont été identifiées dans le processus de recrutement :

-  Un **volume important de candidatures** à traiter manuellement, souvent au format texte libre (CV PDF, lettres de motivation, profils LinkedIn).
-  Un **tri fastidieux** qui repose largement sur la lecture humaine, faute d'outils adaptés au marché local.
-  Des outils existants peu adaptés aux **réalités du marché camerounais** (formulations en français, contexte culturel, profils variés).
-  Une **perte de temps considérable** pour les RH, qui peinent à identifier rapidement les bons profils dans un délai raisonnable.

###  La réponse apportée par l'équipe

Pour adresser ces problématiques, notre équipe développe une **CVthèque automatisée** capable de :

- Centraliser les candidatures,
- Extraire automatiquement les informations clés des profils,
- Faciliter le **matching candidat / offre** pour les recruteurs.

Le projet a été divisé entre plusieurs membres, chacun prenant en charge un module spécifique (parsing, indexation, matching, interface, etc.).

> 🧩 Mon périmètre : la conception et l'implémentation du module d'extraction des soft skills, en partant du texte brut des candidats.

Ce dépôt **ne contient pas** la CVthèque complète — uniquement la brique NLP dont j'ai eu la responsabilité, conçue pour être ensuite intégrée à la plateforme par le reste de l'équipe.

---

## 🎯 Problématique adressée par ce module

Dans une CVthèque classique, la recherche par mots-clés se limite souvent aux **compétences techniques** (hard skills). Or, les **soft skills** — *gestion du stress, esprit d'équipe, rigueur, adaptabilité* — sont rarement explicitées sous forme de mots-clés : elles sont **noyées dans le langage naturel** des candidats.

Pour des recruteurs RH camerounais, qui doivent rapidement filtrer un grand nombre de profils, identifier ces compétences manuellement est particulièrement chronophage.

Ce module vise donc à :

-  Détecter automatiquement les soft skills dans des phrases libres en français




##  Méthodologie & Approche technique

L'approche retenue repose sur un pipeline de **Named Entity Recognition (NER)** personnalisé :

### 1. Annotation des données
Constitution d'un jeu de données d'entraînement spécifique au domaine RH à l'aide de **NER Annotator**, avec annotation manuelle de l'entité personnalisée `SOFT_SKILL`.

### 2. Entraînement du modèle
**Fine-tuning** d'un pipeline **spaCy**  sur le corpus annoté pour spécialiser le modèle dans la reconnaissance des soft skills en langue française.

### 3. Évaluation
Mesure des performances du modèle (precision, recall, F1-score) sur un jeu de validation distinct.

> 📚 **Inspiration méthodologique :** travaux de recherche relatifs à l'extraction d'entités de compétences ([référence Medium](https://medium.com/)).



> Les performances pourront être améliorées en enrichissant le dataset annoté avec davantage de profils issus du marché RH camerounais, et en testant des modèles Transformers (CamemBERT).

---

Stack technique

- Python 
- spaCy — pipeline NLP et fine-tuning NER
- NER Annotator — annotation du dataset
- Pandas — manipulation des données
- Jupyter — prototypage et expérimentation

---


Fotue Mogueo Joyce Audrey
Contribution : module d'extraction des soft skills (NLP / NER)
Projet d'équipe : CVthèque intelligente pour les RH du Cameroun 🇨🇲



