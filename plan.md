
# Plan

### jour 1

Introduction à Python et les fondamentaux du langage.

- Présentation de l'environnement
- Installation (interpréteur python, pip, éditeur?)
- Style et convention (instruction, indentation & more)
- Variables
    - Opérateurs et affectation (+,-,*,**,/,//,%,=)
    - memory management
- Types 
    - builtin (int, float, boolean, string, list, set, tuple, dict)
    - mutabilité et indexation
- Expression conditionnelle
    - branchement (if, elif, else)
    - Opérateur de comparaison (<>, <>=, ==, !=, in, not)
- Exos...
- Boucle  (for, while) 
    - itérations
    - Structure de contrôle (continue, break)
- Exception (try/catch)
- Exos...

### jour 2

- Fonctions
    - builtin functions: print, sum, len, range, sum, map and open
    - user defined
- Exo: **Pour chacune des fonctions ci-dessous, elle doivent pouvoir être exécuté en appelant le script qui les contient, et les arguments passable en ligne de commande.**
    * Créer une fonction qui prend en argument le chemin d'un fichier et affiche son contenue.
    * Créer une fonction qui prend deux arguments, un chemin de fichier (nouveau) et une string, et qui écrit un fichier dans le chemin donnée et contenant la string.
    * Créer une fonction qui prend en argument le chemin d'un fichier existant, et qui insère entre chaque mot, le mot `RTFM`.
    * créer une fonction qui prend un chemin en entrée (string) et qui retourne une list de dictionnaire représentant les fichier.  Le dictionnaire contiendra comme clé, le nom du fichier, sa taille, et is c'est un executable ou non.(see `os.walk`)
- Classe et Objet (méthode, attribut et initialisation)
- Regexp
    - première approche avec `sed` et `grep` (play with files greping, and seding.)
    - expression régulière pour matcher: 
        * une nom en majuscule.
        * une adresse mail.
        * un numéro de téléphone international
        * une adresse IPv4
        * une URL
    - Exos: http and file writing (see module `re`): dowload a file, and replace all URL with www.perdu.com

### jour 

Brief 1:
- Revenir sur le crawler de fichier
    - lire le code suivant : https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
    - contruire le csv à partir du dict.

Brief 2:
- parser de log.
    - using re to extract IP, and Keywords.
    - visualisation avec matplotlib ou plotly.

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
