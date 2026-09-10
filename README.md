
# Nouveau projet serveur

## Contexte

Ce projet a pour objectif de préparer et documenter le déploiement d'une application conteneurisée sur un serveur de production.

Avant le déploiement, les étapes suivantes ont été réalisées :

- Installation et vérification de VirtualBox
- Création d'une machine virtuelle sous Ubuntu Server, qui jouera le rôle du futur serveur de production
- Création de ce dépôt GitHub, destiné à accueillir le code de l'application ainsi que ses fichiers de configuration (Docker, Docker Compose, CI/CD)

## À venir

- Ajout du code applicatif et des fichiers de configuration
- Mise en place du pare-feu et de la sécurité du serveur
- Documentation du déploiement final
## Application conteneurisée

L'application Flask (`app.py`, port 5000) a été conteneurisée avec Docker.

- Image construite avec `docker build -t nouveau-projet-serveur .`
- Conteneur lancé avec `docker run -d -p 5000:5000 --name mon-app nouveau-projet-serveur`
- Testée en local avec `curl http://localhost:5000` → réponse OK

