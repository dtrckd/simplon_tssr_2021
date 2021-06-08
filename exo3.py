import sys

#
# Afficher le contenue d'un fichier
#

def show_file(path):
    f = open(path)
    content = f.read()
    print(content)

    # Ou sur une ligne
    #print(open(path, "r").read())


try:
    # Get the command line argument
    path = sys.argv[1]
except Exception as e:
    print("Path argument is needed")
    exit()

show_file(path)
