# Utiliser dbg() pour faire un break dans votre code.
from pdb import set_trace as dbg
from operator import attrgetter

#
# AStarTuple : Class that represents a tuple of TaquinState, score f and parent parent
# In this implementation the weights are constant and equal 1
#
class AStarTuple:

    def __init__(self, state, f, parent=None):
        self.state = state
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return not (self == other)

def g(node):
    sum = 0
    while node.parent:
        sum += 1
        node = node.parent
    return sum

def path(node):
    states = []
    while node.parent:
        states.append(node.state)
        node = node.parent
    states.append(node.state)
    states.reverse()
    return states

def AStar(start, is_goal, transitions, heuristic, cost):
    
    n = AStarTuple(start, heuristic(start), None)
    open = [n]
    closed = []

    while(1):
        if not open:
            print('Error, open is empty.')
            return -1 # Failure

        n = min(open, key=attrgetter('f'))
        closed.append(n)
        open.remove(n)

        if is_goal(n.state):
            result = path(n)
            return result # Success
        
        for next in transitions(n.state):
            m = AStarTuple(next, g(n) + cost(n.state, next) + heuristic(next), n)

            for o in open:
                if m == o and m.f <= o.f:
                    open.remove(o)
                    open.append(m)

            for c in closed:
                if m == c and m.f <= c.f:
                    closed.remove(c)
                    open.append(m)    

            if m not in open and m not in closed : open.append(m)

def joueur_taquin(start, is_goal, transitions, heuristic):
    def fct_cout(x, y): return 1  
    res = AStar(start, is_goal, transitions, heuristic, fct_cout)
    return res
