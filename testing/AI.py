romania_map ={
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

class GraphProblem(object):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        self.initial=initial
        self.goal=goal
        self.graph = graph

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def goal_test(self,state):
        return state==self.goal


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self,problem):
        return problem.actions(self.state)
    
class Queue:
    """Simple FIFO queue"""
    def __init__(self, element=None):
        self.data = []

    def empty(self):
        return True if len(self.data)==0 else False

    def append(self, element):
        self.data.append(element)

    def extend(self,element):
        self.data.extend(element)

    def insert_all(self, element):
        for i in element:
            self.data.append(i)

    def first(self):
        return self.data[0]

    def pop(self):
        return self.data.pop(0)

    def pop_last(self):
        return self.data.pop(len(self.data)-1)


def breadth_first_search(problem,frontier):
    """[Figure 3.11]"""    
    
    node = Node(problem.initial)
    frontier.append(node)
    explored=set()
    
    while frontier:
        node=frontier.pop()
        if problem.goal_test(node.state):            
            return node
    
        if node.state not in explored:
            explored.add(node.state)
            return node.expand(gp)
            #frontier.extend(node.expand(gp))

        
        
##        for child in node.expand(problem):                        
##            if child.state not in explored and child.state not in frontier.data:                
##                if problem.goal_test(child.state):return child
##                frontier.append(child)




    

gp=GraphProblem("Arad","Bucharest",romania_map)
print(gp.initial ,breadth_first_search(gp,Queue()),gp.goal)

