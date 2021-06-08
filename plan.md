
# Plan

### jour 1

Introduction à Python et les fondementaux du langage.

- Presentation de l'environement
- Installation (interpréteur python, pip, éditeur?)
- Style et convention (instruction, indentation & more)
- Variables
    - Opérateurs et affectation (+,-,*,**,/,//,%,=)
    - memory management
- Types 
    - builtin (int, float, boolean, string, list, set, tuple, dict)
    - mutabilité et indexation
- Expression conditionelle
    - branchement (if, elif, else)
    - Opérateur de comparaison (<>, <>=, ==, !=, in, not)
- Exos...
- Boucle  (for, while) 
    - itérations
    - Structure de controle (continue, break)
- Exception (try/catch)
- Exos...

### jour 2

- Functions
    - builtin fonction: print, sum, len, range, sum, map and open
    - user defined
- Exo: **Pour chacune des fonctions ci dessus, elle doivent pouvoir être executé en appellant le script qui les contient, et les argument passable en ligne de commande.**
    * Créer une fonction qui prend en argument le chemin d'un fichier et affiche son contenue.
    * Creéer une fonction qui prend deux argument, un chemin de fichier (nouveau) est une string, et qui ecrit un fichier dans le chemin donnée contenant la string.
    * Creéer une fonction qui prend en argument le chemin d'un fichier existant, et qui insére entre chaque mot, le mot `RTFM`.
    * créer une fonction qui prend un chemin en entrée (string) et qui retourne un, dictionnaire dont les clés sont tout les sous-chemins des **fichiers**, et la valeurs sont un autre dictionnaire contenant, la taille du fichier et son nombre de ligne.(see `os.walk`)
- Classe et Objet (méthode, attribut et initialisation)
- Regexp
    - premiere approche avec `sed` et `grep` (play with files greping, and sedding.)
    - expression régulière pour matcher: 
        * une nom en majuscule.
        * une addresse mail.
        * un numéro de téléphone international
        * une addresse IPv4
        * une URL
    - Exos: http and file writing (see module `re`): dowload a file, and replace all URL with www.perdu.com

### jour 3

- Introduction a docopt
- exo-brief 1 (ligne de commande, parsing, and data viz)

### Jour 4 & 5

- retour sur notion
- exo brief 2 (crawler, scraper sniffer).
- take a excel/csv and et user entrye (login, password plus groups.)


# Resources

* https://python.developpez.com/tutoriels/cours-python-uni-paris7/#LII-A
* http://fsincere.free.fr/isn/python/cours_python_ch1.php
* https://informatique-python.readthedocs.io/fr/latest/Cours/cours.html
* multiple lien et ressources (parfois redondant) : https://python.developpez.com/tutoriels/cours-python-uni-paris7/#LII-A
* Learn by example: https://www.learnbyexample.org/python/
* documentation: https://docs.python.org/3/
