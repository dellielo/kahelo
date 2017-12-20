#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


PACKAGE_NAME = 'kahelo'
VERSION = "0.0.1"
AUTHOR_NAME = 'Elodie Dellier'
DESCRIPTION = "Kahelo power"

setup(
    name=PACKAGE_NAME,

    # la version du code
    version=VERSION, #citi.__version__,

    # Liste les packages à insérer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),
    author=AUTHOR_NAME,
    # Une description courte
    description=DESCRIPTION,

    # Une description longue, sera affichée pour présenter la lib
    # Généralement on dump le README ici
    long_description=open('README.md').read(),

    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,

    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,

    # # Une url qui pointe vers la page officielle de votre lib
    # url='http://github.com/sametmax/sm_lib',

    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Ideas",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internal functions",
    ],


    # # C'est un système de plugin, mais on s'en sert presque exclusivement
    # # Pour créer des commandes, comme "django-admin".
    # # Par exemple, si on veut créer la fabuleuse commande "proclame-sm", on
    # # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # # créé automatiquement.
    # # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'kahelo_test = kahelo_test:main',
        ],
    },

    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="MIT",
    )
