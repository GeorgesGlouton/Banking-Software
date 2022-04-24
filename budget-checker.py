"""
Check compliance with the established weekly budget.
Rentrer le salaire de Blanche, toutes les dépenses, trier les
dépenses en catégories distinctes.
Epicerie, alcool/clopes, hygiène, vetements, loisirs, manger à
l'extérieur, matériel d'école, autres
Calculer si la dépense du mois est déficitaire, afficher en couleur
distinctes chaque dépense de chaque catégorie
Display le gain/perte
Créer un budget type et mettre en couleur flashy la ou le budget est
bien dépassé et de combien
Voir budget type
Trouver comment garder en mémoire la balance utilisateur
Ajouter option budget Maxime (diviser par deux l'épicerie)
"""

file_handle = open('balance.txt', mode='r')
for line in file_handle:
    content_balance = line.strip()
    balance = float(content_balance)
file_handle.close()

file_handle = open('vault.txt', mode='r')
for line in file_handle:
    content_vault = line.strip()
    vault = float(content_vault)
file_handle.close()

def get_user_input(prompt, parser=str, newline=False):
    """
    Retrieve user input and converts it using `parser`.
    If `newline` is set to `false` (default), append `: ` to the prompt.
    Otherwise, append `\n ` to the prompt.
    """
    while True:
        try:
            if newline:
                print(prompt)
            else:
                print(prompt + " ", end="")
            user_input = input()
            return parser(user_input)
        except ValueError:
            print("Tu as du te tromper, réessaye s'il te plaît.")


name = get_user_input("Bonjour, à qui ai-je l'honneur?", newline=True)
print(f"Bonjour {name}, j'espère que tu vas bien.")
salary = get_user_input("Combien as-tu gagné ce mois-ci?", float)

while True:
    user_input = input("+ \n")
    if user_input.lower() == 'ok':
        break
    else:
        try:
            salary = float(salary) + float(user_input)
            continue
        except ValueError:
            print("Tu as du te tromper, réessaye s'il te plaît")
            continue
print("Très bien, calculons maintenant tes dépenses.")
balance = balance + salary


def categories_calculator(category):
    """
    Input expenses on each category and make sure it's a number.
    """
    total_spending = get_user_input(f"Combien as-tu dépensé en {category}?",
                                    float)
    while True:
        user_input = input("+ \n")
        if user_input.lower() == 'ok':
            break
        else:
            try:
                user_input = float(user_input)
                total_spending = float(total_spending) + user_input
                continue
            except ValueError:
                print("Tu as du te tromper, réessaye s'il te plaît")
                continue
    print("Passons à la catégorie suivante.")
    return total_spending


def balance_comparator(total_spending, budget_of_category, category):
    """
    Compute the difference between the expense of the category and
    its budget. Print the result depending on 3 outcomes.
    """
    balance_of_category = budget_of_category - total_spending
    if balance_of_category == 0:
        print(f"Tu as dépense {round(total_spending, 2)}$ en {category} cette semaine,"
              " pile-poil dans le budget. Bravo!")
    elif balance_of_category > 0:
        print(f"Tu as dépensé {round(total_spending, 2)}$ en {category} cette semaine,"
              f" c'est {round(balance_of_category, 2)}$ d'économisé!")
    else:
        print(f"Tu as dépensé {round(total_spending, 2)}$ en {category} cette semaine,"
              f" c'est {round(balance_of_category * -1, 2)}$ au-dessus du budget.")


balance_epicerie = categories_calculator("épicerie")/2
balance_alcool_clopes = categories_calculator("alcool et cigarettes")
balance_hygiene = categories_calculator("produits d'hygiène et de santé")
balance_vetements = categories_calculator("vêtements")
balance_loisirs = categories_calculator("loisirs")
balance_restaurant = categories_calculator("restaurants")
balance_materiel_ecole = categories_calculator("matériel d'école")
balance_autres = categories_calculator("autres frais")
balance_charges_fixe = 0

while True:
    choice = get_user_input("Est-ce que tu payes des" 
                            " charges fixes ce mois-ci?",
                            str,
                            newline=True)
    if choice.upper() == 'OUI':
        balance_charges_fixes = categories_calculator("charges fixes")
        balance_comparator(balance_charges_fixes, 474, "charges fixes")
        break
    if choice.upper() == 'NON':
        print("Alors passons aux résultats")
        break
    else:
        print("Tu as du te tromper de réponse, essaye avec 'Oui' ou 'Non'")
        continue

balance_comparator(balance_epicerie, 50, "épicerie")
balance_comparator(balance_alcool_clopes, 40, "alcool et cigarettes")
balance_comparator(balance_hygiene, 10, "produits d'hygiène et de santé")
balance_comparator(balance_vetements, 10, "vêtements")
balance_comparator(balance_loisirs, 20, "loisirs")
balance_comparator(balance_restaurant, 20, "restaurants")
balance_comparator(balance_materiel_ecole, 20, "matériel d'école")
balance_comparator(balance_autres, 10, "autres")

balance = float(balance - sum([
    balance_epicerie,
    balance_alcool_clopes,
    balance_hygiene,
    balance_vetements,
    balance_loisirs,
    balance_restaurant,
    balance_materiel_ecole,
    balance_charges_fixe
]))

print(f"Ta balance pour cette semaine est de {round(balance, 2)}$.")

file_handle = open('balance.txt', mode="w")
file_handle.write(str(balance))
file_handle.close()

while True:
    choice = get_user_input("Est-ce que tu veux mettre de l'argent de côté?",
        newline=True)
    if choice.upper() == 'OUI':
        epargne = float(input("Combien? \n"))
        balance = float(balance) - float(epargne)
        vault = float(vault) + float(epargne)
        break
    elif choice.upper() == 'NON:':
        break
    else:
        print("Je n'ai pas compris, réessaye s'il te plaît.")
        continue

print(f"Au total, tu as mis {round(vault, 2)}$ de côté.")
print(f"Ta balance est maintenant de {round(balance, 2)}$")

file_handle = open('vault.txt', mode='w')
file_handle.write(str(vault))
file_handle.close()