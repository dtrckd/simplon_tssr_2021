
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
- Regexp
    - première approche avec `sed` et `grep` (play with files greping, and seding.)
    - expression régulière pour matcher: 
        * une nom en majuscule.
        * une adresse mail.
        * un numéro de téléphone international
        * une adresse IPv4
        * une URL

### jour 3

**Brief 1**
- Réaliser un scanner de dossier avec génération de résulats au format csv.
    - vous devez extraire pour chaque fichier, son nom, sa taille en Ko, si c'est un exécutable et son extension.
    - Example d'utilisatinon du `os.walk` pour scanner un repertoire :  https://docs.microsoft.com/en-us/windows/python/scripting
    - lire le code suivant pour l'enregistrement du fichier csv à partid de dict python : https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
    - contruire le csv à partir du dict.


### Jour 4

**Brief 2**
- parser de log (log fourni. Provenance:  https://zenodo.org/record/3227177)
    - using `re` to extract IP, and Keywords.
    - visualisation d'histogramme avec matplotlib ou plotly.

**Brief 3**
    - Télecharger une page web avec le module `urlopen` (par example `https://wikipedia.org`
    - modifier le contenue de la page et enregister la page en html.
        - remplacer toutes les URL par la suivante `http://www.perdu.com` à l'aide du module `re`.

**Brief 4**
    Decouverte de fabric pour automatiser la creation d'utilisateur sur des machine distance.
    Les données d'entré sont deux fichiers:
    * un tableur des utilisateur à créer (username and name)
    * un tableur des liste de machines (adresse ip)

### Jour  5

- retour sur notions et script.
- Working with an API (virustotal.com).
- decouverte et test avec Ansible.


Notes sur:
- Classe et Objet (méthode, attribut et initialisation)
- Autre modules externes puissants

# Resources

* https://python.developpez.com/tutoriels/cours-python-uni-paris7/#LII-A
* http://fsincere.free.fr/isn/python/cours_python_ch1.php
* https://informatique-python.readthedocs.io/fr/latest/Cours/cours.html
* yet another one (en francais): https://www.pierre-giraud.com/python-apprendre-programmer-cours
* multiple lien et ressources (parfois redondant) : https://python.developpez.com/tutoriels/cours-python-uni-paris7/#LII-A
* Learn by example: https://www.learnbyexample.org/python/
* documentation: https://docs.python.org/3/
