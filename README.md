# Application Sandwich - Gestion de commandes Deli

Projet pédagogique réalisé dans le cadre du **Plan LIBERTAS (Mois 1)**  
**Auteur** : Charles HOUNSOU-KAN  
**Date** : 14/12/2025  

## Objectif du projet

Maîtriser les concepts fondamentaux de Python :
- Les boucles `while`
- La manipulation des listes (`pop`, `append`)
- L'utilisation des dictionnaires avec la méthode `.get()`
- Le traitement et le comptage de commandes

Cet exercice simule la gestion d'une file d'attente de commandes dans un deli (sandwicherie).

## Fonctionnalités

1. **Comptage des commandes initiales**  
   Affiche le nombre de chaque type de sandwich commandé, trié par ordre alphabétique.

2. **Préparation des sandwiches**  
   Traite les commandes une par une (comme une vraie file d'attente) en utilisant une boucle `while` et retire chaque commande de la liste avec `pop(0)`.

3. **Liste des sandwiches terminés**  
   Affiche tous les sandwiches préparés dans l'ordre de fabrication.

4. **Résumé final**  
   Indique le nombre total de sandwiches préparés dans la journée.

## Exemple de sortie du programme

```
=== Commandes initiales ===
fish: 2
jambon: 1
poulet: 1
saucisse: 1
thon: 2
végétarien: 1


J'ai fait ton sanwich au thon !
J'ai fait ton sanwich au poulet !
J'ai fait ton sanwich au thon !
J'ai fait ton sanwich au fish !
J'ai fait ton sanwich au végétarien !
J'ai fait ton sanwich au saucisse !
J'ai fait ton sanwich au jambon !
J'ai fait ton sanwich au fish !

=== Sandwiches préparés aujourd'hui ===
- Sandwich au thon
- Sandwich au poulet
- Sandwich au thon
- Sandwich au fish
- Sandwich au végétarien
- Sandwich au saucisse
- Sandwich au jambon
- Sandwich au fish

 ----- Total sandwiches préparés : 8 -----
```

## Comment exécuter le code

1. Assure-toi d'avoir Python installé (version 3.x).
2. Télécharge ou copie le fichier `exo_chap7_7_8.py`.
3. Exécute-le avec la commande :
```bash
python exo_chap7_7_8.py
```

## Technologies utilisées

- Python
- Structures de données natives (listes et dictionnaires)

## Licence

Ce projet est à usage pédagogique et personnel. Libre de consultation et de réutilisation pour l'apprentissage.

---

Merci d'avoir visité ce dépôt ! Ce projet fait partie de mon apprentissage progressif en programmation Python.  
N'hésite pas à laisser une étoile ⭐ ou un commentaire si cela t'a été utile !
