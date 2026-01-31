# FRUIT SLICER

Un jeu de tranchage de fruits inspiré de Fruit Ninja, développé en Python avec Pygame.

## Description

Fruit Slicer Pro est un jeu d'arcade où vous devez trancher des fruits en évitant les bombes. Le jeu propose deux modes de jeu, trois niveaux de difficulté et un support multilingue (français/anglais).

## Fonctionnalités

- **Deux modes de jeu :**
  - **Classique** : Évitez de laisser tomber 3 fruits pour ne pas perdre
  - **Challenge** : Marquez un maximum de points en 60 secondes

- **Trois niveaux de difficulté :**
  - Facile
  - Normal
  - Difficile

- **Objets spéciaux :**
  - **Fruits normaux** : +1 point
  - **Bombes** : Game Over immédiat
  - **Glaçons** : Ralentissent le jeu pendant quelques secondes
  - **Fruits dorés** : +5 points

- **Bonus de combo** : Tranchez plusieurs fruits d'un coup pour des points bonus
- **Support multilingue** : Français et anglais
- **Système de high score**

## Prérequis

- Python 3.x
- Pygame

## Installation

1. Clonez ce dépôt ou téléchargez le fichier
2. Installez Pygame si ce n'est pas déjà fait :
```bash
pip install pygame
```

## Lancement du jeu
```bash
python fruit_slicer.py
```

## Comment jouer

1. Lancez le jeu et cliquez sur **JOUER**
2. Utilisez votre souris pour trancher les fruits
3. Évitez les bombes noires à tout prix !
4. Récupérez les glaçons pour ralentir le temps
5. Visez les fruits dorés pour plus de points
6. En mode Classique : ne laissez pas tomber 3 fruits
7. En mode Challenge : faites le meilleur score en 60 secondes

## Commandes

- **Clic gauche** : Trancher les fruits
- **Menu** : Navigation par clic sur les boutons

## Système de score

- Fruit normal : **1 point**
- Fruit doré : **5 points**
- Combo de 2 fruits : **+1 point bonus**
- Combo de 3 fruits : **+2 points bonus**
- Et ainsi de suite...

## Configuration

Les paramètres du jeu peuvent être modifiés dans la section `CONFIGURATION & CONSTANTES` du code :

- `SCREEN_WIDTH` / `SCREEN_HEIGHT` : Dimensions de la fenêtre
- `GRAVITY` : Force de gravité appliquée aux objets
- Couleurs personnalisables


## Développement

Développé avec Python et Pygame.

---

**Amusez-vous bien !**
EOF
