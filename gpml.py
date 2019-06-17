import ndex2
import networkx as nx
from lxml import etree as ET

NAMESPACES = {'ns1':'http://www.wso2.org/php/xsd','ns2':'http://www.wikipathways.org/webservice/', 'ns3': "http://pathvisio.org/GPML/2013a"}

# read gpml file
gpml_file = 'WP289_102527.gpml'
dom = ET.parse(gpml_file)

G = nx.MultiDiGraph()

for node in dom.findall('ns3:DataNode', NAMESPACES):
    id = node.get('GraphId')
    G.add_node(id)
    node_attributes = dict()
    node_attributes[id] = dict(node.attrib)
    nx.set_node_attributes(G, node_attributes)
#    for name, value in sorted(node.items()):
#        print('%s = %r' % (name, value))

for node in dom.findall('ns3:Shape', NAMESPACES):
    id = node.get('GraphId')
    G.add_node(id)
    node_attributes = dict()
    node_attributes[id] = dict(node.attrib)
    nx.set_node_attributes(G, node_attributes)

for node in dom.findall('ns3:Label', NAMESPACES):
    id = node.get('GraphId')
    G.add_node(id)
    node_attributes = dict()
    node_attributes[id] = dict(node.attrib)
    nx.set_node_attributes(G, node_attributes)

#for node in dom.findall('ns3:Group', NAMESPACES):
#    id = node.get('GraphId')
#    G.add_node(id)

for edge in dom.findall('ns3:Interaction', NAMESPACES):
    id = edge.get('GraphId')
    edge_attributes = dict(edge.attrib)
    for graphics in edge.findall('ns3:Graphics', NAMESPACES):
        for name, value in sorted(graphics.items()):
            print('%s = %r' % (name, value))
            edge_attributes[name] = value

        for anchor in graphics.findall('ns3:Anchor', NAMESPACES):
            anchor_id = anchor.get('GraphId')
            G.add_node(anchor_id)
            node_attributes = dict()
            node_attributes[anchor_id] = dict(node.attrib)
            nx.set_node_attributes(G, node_attributes)

        points = list()
        for point in graphics.findall('ns3:Point', NAMESPACES):
            GraphRef = point.get('GraphRef')
            print(GraphRef)
            points.append(GraphRef)

        key = G.add_edge(points[0], points[-1])
        print(key)
        print(type(key))

        keyed_edge_attributes = dict()
        keyed_edge_attributes[key] = edge_attributes
        print(keyed_edge_attributes)

#        # TODO: these are not working
#        G[points[0]][points[-1]].update({0: 5})
#        G[points[0]][points[-1]].update(edge_attributes)
#        nx.set_edge_attributes(G, keyed_edge_attributes)

#    <Graphics ZOrder="12288" LineThickness="1.0" Color="ff0080">
#      <Point X="740.0" Y="170.0" GraphRef="aa684" RelX="0.0" RelY="1.0" />
#      <Point X="740.0" Y="210.0" GraphRef="cd799" RelX="0.0" RelY="-1.0" ArrowHead="Arrow" />
#      <Anchor Position="0.675" Shape="None" GraphId="b7b89" />
#      <Anchor Position="0.5" Shape="None" GraphId="fdd58" />
#    </Graphics>

print(G)
print(type(G))
print(nx.info(G))
