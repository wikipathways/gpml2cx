import ndex2
import networkx as nx
import matplotlib.pyplot as plt
import os

print(os.environ['NDEX_USER'])
NDEX_USER=os.environ['NDEX_USER']
NDEX_PWD=os.environ['NDEX_PWD']

G = nx.MultiDiGraph()

id = 1
G.add_node(id)
node_attributes = dict()
node_attributes[id] = {"pos": '100,100', "color": 'green', 'label': 1}
nx.set_node_attributes(G, node_attributes)

id = 2
G.add_node(id)
node_attributes = dict()
node_attributes[id] = {"pos": '100,200', "color": 'blue', 'label': 2}
nx.set_node_attributes(G, node_attributes)

id = 3
G.add_node(id)
node_attributes = dict()
node_attributes[id] = {"pos": '300,200', "color": 'red', 'label': 3}
nx.set_node_attributes(G, node_attributes)

id = 4
G.add_node(id)
node_attributes = dict()
node_attributes[id] = {"pos": '250,50', "color": 'black', 'label': 1}
nx.set_node_attributes(G, node_attributes)

key = G.add_edge(1, 2)
G[1][2][key]['weight'] = 5

key = G.add_edge(2, 3)
G[2][3][key]['weight'] = 2
G[2][3][key]['pos'] = {'v': (200, 200), 'd': 'list_of_integer'}

#key = G.add_edge(1, (1, 3, key))
key = G.add_edge(1, 4)

#S = nx.Graph(subgraph_edges)

#key = G.add_edge(1, 2)
#G[1][2][key]['weight'] = 5

#keyed_edge_attributes = dict()
#keyed_edge_attributes[key] = {"weight": 30, "color": 'red'}

print(nx.info(G))

#pos=nx.get_node_attributes(G,'pos')
#node_positions = {1: (10, 10), 2: (10, 20), 3: (30, 20), (1, 3, key): (20, 20)}
#node_labels = {1: 1, 2: 2, 3: 3, (1, 3, key): 'anchor'}

node_positions = {1: (100, 100), 2: (100, 200), 3: (300, 200), 4: (250, 50)}
node_labels = {1: 1, 2: 2, 3: 3, 4: 'dummy'}

node_color=[1, 4, 4, 3]

G.pos = node_positions

nx.draw(G, node_positions)
nx.draw_networkx_nodes(G, pos=node_positions, node_color=node_color)
nx.draw_networkx_labels(G, node_positions, node_labels)

#plt.show() # display

G.name = 'Created from NetworkX (full)'
nice_cx_full = ndex2.create_nice_cx_from_networkx(G)

nice_cx_full.print_summary()
print(G.edges())
print('')

mycx = nice_cx_full.to_cx()
print(mycx)

#nice_cx_full.apply_template(server='http://test.ndexbio.org',
#        username=NDEX_USER,
#        password=NDEX_PWD,
#        uuid='e75236d5-8275-11e9-b14c-0660b7976219')

style_network = ndex2.create_nice_cx_from_file('./WP4571.cx.json')
nice_cx_full.apply_style_from_network(style_network)

print('')

mycx = nice_cx_full.to_cx()
print(mycx)

#result = nice_cx_full.upload_to(server='http://test.ndexbio.org', username=NDEX_USER, password=NDEX_PWD)

result = nice_cx_full.update_to(server='http://test.ndexbio.org',
        username=NDEX_USER,
        password=NDEX_PWD,
        uuid='5631c7dd-8278-11e9-b14c-0660b7976219')

print(result)

# another example of using this
#G.name = 'Created from NetworkX (shortest path)'
#nice_cx_short = ndex2.create_nice_cx_from_networkx(path_subgraph)
#
#nice_cx_short.print_summary()
#print(path_subgraph.edges())
