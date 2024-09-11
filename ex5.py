#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

letters = [x for x in code_medals]
medals = ["G", "S", "B"]
new_code = []

for lettre in letters:
    if lettre in medals:
        new_code.append(lettre)

    else:
        print("Veuillez entrer une chaîne valide.")
        break

if len(new_code) >= 1:
    count_G = new_code.count("G")
    count_S = new_code.count("S")
    count_B = new_code.count("B")

    print(f"{country}:\n- {count_G} OR\n- {count_S} Argent\n- {count_B} Bronze")

