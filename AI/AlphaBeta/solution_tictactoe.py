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


def alpha_beta(state, fct_goal, fct_transitions, str_player, alpha=float("-inf"), beta = float("inf")):

    if(fct_goal(state)):
        return fct_goal(state), None

    if(str_player == 'X'):
        max_eval = float('-inf')
        next_action = None

        for a, s in fct_transitions(state).items():
            candidate_score, _ = alpha_beta(s, fct_goal, fct_transitions, 'O', alpha, beta)

            # Update local maximum
            if(max_eval < candidate_score):
                max_eval = candidate_score
                next_action = a
            
						# Pruning
            if(beta <= alpha):
                return max_eval, next_action

            # Update global maximum
            alpha = max(alpha, candidate_score)

        return max_eval, next_action

    else:
        min_eval = float('inf')
        next_action = None

        for a, s in fct_transitions(state).items():
            candidate_score, _ = alpha_beta(s, fct_goal, fct_transitions, 'X', alpha, beta)

            # Update local minimum
            if(min_eval > candidate_score):
                min_eval = candidate_score
                next_action = a
            
			# Pruning
            if(beta <= alpha):
                return min_eval, next_action

            # Update global minimum
            beta = min(candidate_score, beta)

        return min_eval, next_action


def joueur_tictactoe(etat, fct_but, fct_transitions, str_joueur):
    return alpha_beta(etat, fct_but, fct_transitions, str_joueur)[1]