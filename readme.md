last_update: 08-11-2023

language: fr
Langue: Francais

Programme: 
1 calcule le prix_TTC à partir d'un prix_HT et une TVA appliée
2 - une campagne de tests automatisée

inputs:
prix: un float non nul
TVA: un float entre 0.01 et 100

output:
ptix TTC

Pour lancer le programme: main.py
Pour lancer les tests: teste.py

prerequis:
Docker:
    builder une image {image}
    docker build -t {image} .

    Pour lancer le programme:
    docker run -it tptp1 python src/main.py {prix} {TVA}

    pour lancer la campagne des tests automatisée:
    docker run -it tptp1 python src/teste.py

local (Python 3 est requis):
1 se mettre au dossier du projet (tp-docker)

2
 pour lancer le programe à partir du terminal: 
    python src/main.py {prix} {TVA}

 Pour lancer la campagne des tests:
    python src/teste.py 
