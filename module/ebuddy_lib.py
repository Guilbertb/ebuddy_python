import socket,os,time

def init_ebuddy():
    global ebuddy_state
    ebuddy_state=0
    ebuddy(ebuddy_state)

def ebuddy(ordre):
    chaine = 'ebuddy/ebuddy '+str(ordre)
    os.system(chaine)
    global ebuddy_state
    ebuddy_state=ordre
    #print (ebuddy_state)
    return


def ebuddy_coeur(etat):
    global ebuddy_state
    if etat==1 :
        ebuddy_state=ebuddy_state|128
        ebuddy(ebuddy_state)
    else:
        ebuddy_state=ebuddy_state&~128
        ebuddy(ebuddy_state)
    return


def ebuddy_tete(couleur):
#8 couleurs possibles rouge vert bleu ! le blanc est plutot bleu ici
    global ebuddy_state
    ebuddy_state = ebuddy_state & (~7<<4)        
    ebuddy_state = ebuddy_state | couleur<<4
    ebuddy(ebuddy_state)
    return

def ebuddy_ailes(pos):
    global ebuddy_state
    ebuddy_state = ebuddy_state & (~3<<2)
    ebuddy_state = ebuddy_state | pos<<2
    ebuddy(ebuddy_state)
    return

def ebuddy_corps(pos):
    global ebuddy_state
    ebuddy_state = ebuddy_state & (~3<<0)
    ebuddy_state = ebuddy_state | pos<<0
    ebuddy(ebuddy_state)
    return

