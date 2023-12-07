import networkx as nx
import matplotlib.pyplot as plt
# %matplotlib inline


AGraph = nx.Graph()

Nodes = range(1, 6)
Edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (4, 5)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

AGraph.add_node(6)
sorted(nx.connected_components(AGraph),)

AGraph.add_edge(5, 6)
sorted(nx.connected_components(AGraph),)

nx.degree_centrality(AGraph)

nx.draw(AGraph, with_labels=True, node_color='yellow', node_size=800, edge_color='red')
plt.show()

