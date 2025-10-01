#>>>import random, string, os
#>>>"".join([random.choice(string.printable) for _ in os.urandom(24) ] )
SECRET_KEY = "e422bc18-3e6c-4cbd-b7b3-4d3c68141aca"
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Contactez-moi à l'adresse email suivante :"

BOOTSTRAP_SERVE_LOCAL = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')