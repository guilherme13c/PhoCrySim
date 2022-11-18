import components
import networkx as nx
from typing import List, Tuple
import matplotlib.pyplot as plt

class Circuit:
    def __init__(self, inputs:List=[], gates:List=[], readers:List=[], connections:List[Tuple]=[]):
        self.inputs = inputs
        self.gates = gates
        self.readers = readers
        self.connections = connections
        self.g = nx.DiGraph(name="circuit representation")
        self.g.add_nodes_from(inputs+gates+readers)
        self.g.add_edges_from(connections)

    def addComponent(self, component, connections):
        self.g.add_node(component)
        for c in connections:
            self.g.add_edge(c)  

    def showDiagram(self):
        l = self.inputs+self.gates+self.readers
        labels = {}
        for i in range(len(l)):
            labels[i] = l[i]
        
        print(l)
        print(labels)
        
        nx.draw_networkx(self.g, edge_color='k', with_labels=True)
        plt.show()


