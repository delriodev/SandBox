# -*- coding: utf-8 -*-

#####
# Daniel del Rio Devora (18076519)
# Michael Durand-Chorel (17141086)
###

from pdb import set_trace as dbg  # Utiliser dbg() pour faire un break dans votre code.

import random
import numpy as np

########################
# Solution tic-tac-toe #
########################

#####
# joueur_tictactoe : Fonction qui calcule le prochain coup optimal pour gagner la
#                     la partie de Tic-tac-toe à l'aide d'Alpha-Beta Prunning.
#
# etat: Objet de la classe TicTacToeEtat indiquant l'état actuel du jeu.
#
# fct_but: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#          qui retourne le score actuel tu plateau. Si le score est positif, les 'X' ont l'avantage
#          si c'est négatif ce sont les 'O' qui ont l'avantage, si c'est 0 la partie est nulle.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#                   qui retourne une liste de tuples actions-états voisins pour l'état donné.
#
# str_joueur: String indiquant c'est à qui de jouer : les 'X' ou 'O'.
#
# retour: Cette fonction retourne l'action optimal à jouer pour le joueur actuel c.-à-d. 'str_joueur'.
###


def joueur_tictactoe(etat,fct_but,fct_transitions,str_joueur):

    alpha = -float("inf")
    beta = float("inf")


    def tour_max(etat, alpha, beta):

        if fct_but(etat) is not None:
           return fct_but(etat), None
        
        u = -float("inf")
        a = None

        for action,e in fct_transitions(etat).items():
           
            utility,_ = tour_min(e, alpha, beta)

            if  utility > u:
                a = action
                u = utility

            if u >= beta:
                return u,a

            alpha = max(alpha, u)

        return u,a

    def tour_min(etat, alpha, beta):

        if fct_but(etat) is not None:
            return fct_but(etat), None

        u = float("inf")
        a = None

        for action,e in fct_transitions(etat).items():

            utility,_ = tour_max(e, alpha, beta)

            if utility < u:
                a = action
                u = utility

            if u <= alpha:
                return u,a
            
            beta = min(beta, u)
        
        return u,a


    if str_joueur == 'X':
        _,action = tour_max(etat, alpha, beta)
    else:
        _,action = tour_min(etat, alpha, beta)


    return action