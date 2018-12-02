#!/usr/bin/python
from module.ebuddy_lib import *

#initialisation du ebuddy 
init_ebuddy()

# 2 etats le coeur allumé ou éteint
ebuddy_coeur(1)
ebuddy_coeur(0)
# couleurs de la tete 
#1 : 001 rouge 
#2 : 010 vert
#3 : 011 rouge + vert
#4 : 100 bleu 
#5 : 101 bleu + rouge 
#6 : 110 bleu + vert
#7 : 111 bleu mais on attends du blanc.. , probleme de bleu (trop)
rouge=1
vert=2
bleu=4
ebuddy_tete(rouge + vert + bleu)  # bleu (blanc)
# les ailes
#0 : neutre
#1 : ailes hautes
#2 : ailes basses
#3 : valeur interdite 
haut=1
bas=2
ebuddy_ailes(haut)

# le corps
#0 : neutre
#1 : a droite
#2 : a gauche
#3 : valeur interdite 
droite=1
gauche=2
ebuddy_corps(droite)