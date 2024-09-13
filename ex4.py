# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))
if battery_level > 100 or battery_level < 0:
    print("Valeur non valide")

elif battery_level > 50:
    distance = 2*(battery_level - 50) + 25*0.5 + 15 + 5*2.5 + 5*6

elif battery_level > 25:
    distance = 0.5*(battery_level -25) + 15 + 5*2.5 + 5*6

elif battery_level > 10:
    distance = (battery_level - 10) + 5*2.5 + 5*6

elif battery_level > 5:
    distance = 2.5*(battery_level - 5) + 5*6

else:
    distance = 6*battery_level

if battery_level > 0 and battery_level <= 100:
    print(f"{distance:.1f} km")

elif battery_level == 0:
    print("La batterie est vide")




