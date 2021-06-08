import sys

#
# Create a bunch of user files
#

n_files = int(sys.argv[1])

def create_files(n):
    for i in range(1, n+1):
        fn = "test" + str(i) + ".txt"
        f = open(fn, "w")
        content = "username: user{i}\npassword: user{i}".format(i=i)
        f.write(content)

create_files(n_files)
