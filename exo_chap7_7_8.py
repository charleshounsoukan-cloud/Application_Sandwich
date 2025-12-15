# En-tête 
"""
Programme : Exo 7-8 Deli - Gestion commandes sandwiches
Auteur    : [Charles HOUNSOU-KAN] - Plan LIBERTAS Mois 1
Date      : 14/12/2025
Objectif  : Maîtriser while + listes pour traiter commandes
"""

sandwichs_orders = ['thon', 'poulet', 'thon', 'fish', 'végétarien', 'saucisse', 'jambon', 'fish']
finished_sandwiches = []

commandes_count = {}
for order in sandwichs_orders:
    # Intégration de .get() : si order existe, ajoute 1, sinon commence à 0
    commandes_count[order] = commandes_count.get(order, 0) + 1 

print("=== Commandes initiales ===")
for sandwich, count in sorted(commandes_count.items()):
    print(f"{sandwich}: {count}")

print("\n")

while sandwichs_orders:
    current_sandwich = sandwichs_orders.pop(0) #prend le premier de la liste (comme une file d'attente)
    print(f"J'ai fait ton sanwich au {current_sandwich} !")
    finished_sandwiches.append(current_sandwich)
print("\n=== Sandwiches préparés aujourd'hui ===")
for sandwich in finished_sandwiches:
    print(f"- Sandwich au {sandwich}")
print(f"`\n ----- Total sandwiches préparés : {len(finished_sandwiches)} -----")











