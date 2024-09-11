# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math
water_quantity = input("Quelle quantité d'eau faut-il assainir ? ")
filtre = math.ceil(float(water_quantity)/5)
lampe = math.ceil((float(water_quantity)/5)*3)
chlore = float(water_quantity)/10

answer = f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {filtre}\n
        \t- Lampe(s) UV : {lampe}\n
        \t- Chlore : {chlore}kg\n"""
print(answer)