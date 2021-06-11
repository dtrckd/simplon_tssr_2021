from fabric.api import run, local, env

env.user = "YOUR_USERNAME"
env.hosts = ["IP1", "IP2"] # examepl ["1.1.1.1"]

# Utilisation: fab uptime
def uptime():
  run('uptime')

