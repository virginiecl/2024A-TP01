#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

letters = [x for x in code_medals]
medals = ["G", "S", "B"]
wrong = []

for i in range(0, len(letters)):
    if letters[i] not in medals:
        wrong.append(letters[i])

if len(wrong) > 0:
    print("Veuillez entrer une chaîne valide.")
else:
    count_G = letters.count("G")
    count_S = letters.count("S")
    count_B = letters.count("B")

    print(f"{country}:\n- {count_G} OR\n- {count_S} Argent\n- {count_B} Bronze")
