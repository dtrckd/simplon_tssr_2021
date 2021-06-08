import sys

#
# Créer un fichier avec du contenue
#

def create_file(path, content):
    f = open(path, "w")
    f.write(content)

try:
    # Get the command line argument
    path = sys.argv[1]
    content = sys.argv[2]
except as e:
    print("Path and Content argument are needed")
    exit()


create_file(path, content)
