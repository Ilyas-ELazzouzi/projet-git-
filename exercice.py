# Initialisation de la liste des tâches
todos = []

while True:
    # Afficher le menu principal
    print("\n==== Menu ====")
    print("1: Afficher les tâches")
    print("2: Ajouter une tâche")
    print("3: Supprimer une tâche")
    print("q: Quitter")
    print("================")

    # Demander un choix
    choix = input("=> Choisissez une option : ")

    # Gérer les choix
    if choix == "1":
        # Afficher les tâches
        if not todos:
            print("\nLa liste de tâches est vide.")
        else:
            print("\nListe des tâches :")
            for i in range(len(todos)):  # Boucle sur les indices
                print(f"{i + 1}. {todos[i]}")  # Affiche avec une numérotation à partir de 1

    elif choix == "2":
        # Ajouter une tâche
        nouvelle_tache = input("Entrez la nouvelle tâche : ")
        todos.append(nouvelle_tache)
        print(f"Tâche ajoutée : {nouvelle_tache}")

    elif choix == "3":
        # Supprimer une tâche
        if not todos:
            print("\nLa liste de tâches est vide.")
        else:
            print("\nListe des tâches :")
            for i in range(len(todos)):
                print(f"{i + 1}. {todos[i]}")

            # Boucle pour s'assurer que l'entrée est valide
            num = input("Entrez le numéro de la tâche à supprimer : ")
            if num.isdigit():  # Vérifie si l'entrée est un nombre
                num = int(num)
                if 1 <= num <= len(todos):  # Vérifie si le numéro est valide
                    tache_supprimee = todos.pop(num - 1)
                    print(f"Tâche supprimée : {tache_supprimee}")
                else:
                    print("Numéro invalide.")
            else:
                print("Veuillez entrer un numéro valide.")
    elif choix == "q":
        # Quitter le programme
        print("Au revoir !")
        break

    else:
        print("Option invalide, veuillez réessayer.")
