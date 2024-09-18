# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
g = 9.8
distance = round(((speed**2)*(math.sin(math.radians(angle*2))))/g ,2)

print(f"Distance parcourue: {distance}m")
