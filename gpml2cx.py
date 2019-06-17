from ndex2.nice_cx_network import NiceCXNetwork
from lxml import etree as ET
import os

# import ndex2.client as nc
# import ndex2
# import networkx as nx

NAMESPACES = {
    "ns1": "http://www.wso2.org/php/xsd",
    "ns2": "http://www.wikipathways.org/webservice/",
    "ns3": "http://pathvisio.org/GPML/2013a",
}

NDEX_USER = os.environ["NDEX_USER"]
NDEX_PWD = os.environ["NDEX_PWD"]

entities_by_id = dict()
dummy_entities = list()

# read gpml file
gpml_file = "WP289_102527.gpml"
dom = ET.parse(gpml_file)

cx_network = NiceCXNetwork()
gpml_pathway = dom.getroot()
cx_network.set_name(gpml_pathway.get("Name"))


def set_visual_properties_aspect(self, visual_props_aspect):
    """
    Replaces existing visual properties with data passed in.
    This method will update meta data and remove all visual aspects
    setting the new data to :py:const:`~.NiceCXNetwork.CY_VISUAL_PROPERTIES`
    aspect
    :param visual_props_aspect:
    :return:
    """
    if visual_props_aspect is None:
        raise TypeError("Visual Properties aspect is None")

    self.set_opaque_aspect(NiceCXNetwork.CY_VISUAL_PROPERTIES, visual_props_aspect)
    properties = [
        {
            "properties_of": "network",
            "applies_to": 151,
            "view": 151,
            "properties": {
                "NETWORK_ANNOTATION_SELECTION": "false",
                "NETWORK_BACKGROUND_PAINT": "#FFFFFF",
                "NETWORK_CENTER_X_LOCATION": "0.0",
                "NETWORK_CENTER_Y_LOCATION": "0.0",
                "NETWORK_CENTER_Z_LOCATION": "0.0",
                "NETWORK_DEPTH": "0.0",
                "NETWORK_EDGE_SELECTION": "true",
                "NETWORK_HEIGHT": "400.0",
                "NETWORK_NODE_SELECTION": "true",
                "NETWORK_SCALE_FACTOR": "1.0",
                "NETWORK_SIZE": "550.0",
                "NETWORK_WIDTH": "550.0",
            },
        },
        {
            "properties_of": "nodes:default",
            "applies_to": 151,
            "view": 151,
            "properties": {
                "COMPOUND_NODE_PADDING": "10.0",
                "COMPOUND_NODE_SHAPE": "ROUND_RECTANGLE",
                "NODE_BORDER_PAINT": "#CCCCCC",
                "NODE_BORDER_STROKE": "SOLID",
                "NODE_BORDER_TRANSPARENCY": "255",
                "NODE_BORDER_WIDTH": "1.0",
                "NODE_CUSTOMGRAPHICS_1": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_2": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_3": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_4": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_5": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_6": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_7": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_8": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_9": "org.cytoscape.ding.customgraphics.NullCustomGraphics,0,[ Remove Graphics ],",
                "NODE_CUSTOMGRAPHICS_POSITION_1": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_2": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_3": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_4": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_5": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_6": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_7": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_8": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_POSITION_9": "C,C,c,0.00,0.00",
                "NODE_CUSTOMGRAPHICS_SIZE_1": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_2": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_3": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_4": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_5": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_6": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_7": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_8": "50.0",
                "NODE_CUSTOMGRAPHICS_SIZE_9": "50.0",
                "NODE_CUSTOMPAINT_1": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_1, name=Node Custom Paint 1)",
                "NODE_CUSTOMPAINT_2": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_2, name=Node Custom Paint 2)",
                "NODE_CUSTOMPAINT_3": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_3, name=Node Custom Paint 3)",
                "NODE_CUSTOMPAINT_4": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_4, name=Node Custom Paint 4)",
                "NODE_CUSTOMPAINT_5": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_5, name=Node Custom Paint 5)",
                "NODE_CUSTOMPAINT_6": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_6, name=Node Custom Paint 6)",
                "NODE_CUSTOMPAINT_7": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_7, name=Node Custom Paint 7)",
                "NODE_CUSTOMPAINT_8": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_8, name=Node Custom Paint 8)",
                "NODE_CUSTOMPAINT_9": "DefaultVisualizableVisualProperty(id=NODE_CUSTOMPAINT_9, name=Node Custom Paint 9)",
                "NODE_DEPTH": "0.0",
                "NODE_FILL_COLOR": "#FFFFFF",
                "NODE_HEIGHT": "35.0",
                "NODE_LABEL_COLOR": "#000000",
                "NODE_LABEL_FONT_FACE": "SansSerif.plain,plain,12",
                "NODE_LABEL_FONT_SIZE": "12",
                "NODE_LABEL_POSITION": "C,C,c,0.00,0.00",
                "NODE_LABEL_TRANSPARENCY": "255",
                "NODE_LABEL_WIDTH": "200.0",
                "NODE_NESTED_NETWORK_IMAGE_VISIBLE": "true",
                "NODE_PAINT": "#1E90FF",
                "NODE_SELECTED": "false",
                "NODE_SELECTED_PAINT": "#FFFF00",
                "NODE_SHAPE": "ELLIPSE",
                "NODE_SIZE": "35.0",
                "NODE_TRANSPARENCY": "255",
                "NODE_VISIBLE": "true",
                "NODE_WIDTH": "75.0",
                "NODE_X_LOCATION": "0.0",
                "NODE_Y_LOCATION": "0.0",
                "NODE_Z_LOCATION": "0.0",
            },
            "dependencies": {
                "nodeCustomGraphicsSizeSync": "true",
                "nodeSizeLocked": "false",
            },
            "mappings": {
                "NODE_BORDER_PAINT": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=Color,T=string",
                },
                "NODE_BORDER_WIDTH": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=BorderThickness,T=double",
                },
                "NODE_FILL_COLOR": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=FillColor,T=string",
                },
                "NODE_HEIGHT": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=Height,T=double",
                },
                "NODE_LABEL": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=name,T=string",
                },
                "NODE_LABEL_COLOR": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=Color,T=string",
                },
                "NODE_LABEL_FONT_FACE": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=LabelFont,T=string",
                },
                "NODE_LABEL_FONT_SIZE": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=LabelSize,T=double",
                },
                "NODE_SHAPE": {
                    "type": "DISCRETE",
                    "definition": "COL=Shape,T=string,K=0=Hexagon,V=0=HEXAGON,K=1=Ellipse,V=1=ELLIPSE,K=2=RoundRectangle,V=2=ROUND_RECTANGLE,K=3=Oval,V=3=ELLIPSE,K=4=Rectangle,V=4=RECTANGLE,K=5=Triangle,V=5=TRIANGLE,K=6=Pentagon,V=6=HEXAGON,K=7=Organelle,V=7=ROUND_RECTANGLE,K=8=Octagon,V=8=OCTAGON,K=9=RoundedRectangle,V=9=ROUND_RECTANGLE",
                },
                "NODE_TRANSPARENCY": {
                    "type": "DISCRETE",
                    "definition": "COL=Transparent,T=string,K=0=true,V=0=0,K=1=false,V=1=255",
                },
                "NODE_WIDTH": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=Width,T=double",
                },
            },
        },
        {
            "properties_of": "edges:default",
            "applies_to": 151,
            "view": 151,
            "properties": {
                "EDGE_CURVED": "true",
                "EDGE_LABEL_COLOR": "#000000",
                "EDGE_LABEL_FONT_FACE": "Dialog.plain,plain,10",
                "EDGE_LABEL_FONT_SIZE": "10",
                "EDGE_LABEL_TRANSPARENCY": "255",
                "EDGE_LABEL_WIDTH": "200.0",
                "EDGE_LINE_TYPE": "SOLID",
                "EDGE_PAINT": "#323232",
                "EDGE_SELECTED": "false",
                "EDGE_SELECTED_PAINT": "#FF0000",
                "EDGE_SOURCE_ARROW_SELECTED_PAINT": "#FFFF00",
                "EDGE_SOURCE_ARROW_SHAPE": "NONE",
                "EDGE_SOURCE_ARROW_SIZE": "6.0",
                "EDGE_SOURCE_ARROW_UNSELECTED_PAINT": "#000000",
                "EDGE_STROKE_SELECTED_PAINT": "#FF0000",
                "EDGE_STROKE_UNSELECTED_PAINT": "#848484",
                "EDGE_TARGET_ARROW_SELECTED_PAINT": "#FFFF00",
                "EDGE_TARGET_ARROW_SHAPE": "NONE",
                "EDGE_TARGET_ARROW_SIZE": "6.0",
                "EDGE_TARGET_ARROW_UNSELECTED_PAINT": "#000000",
                "EDGE_TRANSPARENCY": "255",
                "EDGE_UNSELECTED_PAINT": "#404040",
                "EDGE_VISIBLE": "true",
                "EDGE_WIDTH": "2.0",
            },
            "dependencies": {"arrowColorMatchesEdge": "true"},
            "mappings": {
                "EDGE_LINE_TYPE": {
                    "type": "DISCRETE",
                    "definition": "COL=LineStyle,T=string,K=0=Dashed,V=0=LONG_DASH,K=1=Dots,V=1=DOT,K=2=Double,V=2=PARALLEL_LINES,K=3=Solid,V=3=SOLID",
                },
                "EDGE_SOURCE_ARROW_SHAPE": {
                    "type": "DISCRETE",
                    "definition": "COL=StartArrow,T=string,K=0=Arrow,V=0=DELTA,K=1=mim-branching-right,V=1=CROSS_OPEN_DELTA,K=2=mim-covalent-bond,V=2=CROSS_DELTA,K=3=mim-branching-left,V=3=CROSS_DELTA,K=4=mim-transcription-translation,V=4=DELTA,K=5=mim-binding,V=5=ARROW,K=6=Line,V=6=NONE,K=7=mim-cleavage,V=7=DIAMOND,K=8=mim-gap,V=8=DELTA,K=9=mim-stimulation,V=9=OPEN_DELTA,K=10=mim-catalysis,V=10=OPEN_CIRCLE,K=11=mim-inhibition,V=11=T,K=12=TBar,V=12=T,K=13=mim-modification,V=13=DELTA,K=14=mim-necessary-stimulation,V=14=CROSS_OPEN_DELTA,K=15=mim-conversion,V=15=DELTA",
                },
                "EDGE_TARGET_ARROW_SHAPE": {
                    "type": "DISCRETE",
                    "definition": "COL=EndArrow,T=string,K=0=Arrow,V=0=DELTA,K=1=mim-branching-right,V=1=CROSS_OPEN_DELTA,K=2=mim-covalent-bond,V=2=CROSS_DELTA,K=3=mim-branching-left,V=3=CROSS_DELTA,K=4=mim-transcription-translation,V=4=DELTA,K=5=mim-binding,V=5=ARROW,K=6=Line,V=6=NONE,K=7=mim-cleavage,V=7=DIAMOND,K=8=mim-gap,V=8=DELTA,K=9=mim-stimulation,V=9=OPEN_DELTA,K=10=mim-catalysis,V=10=OPEN_CIRCLE,K=11=mim-inhibition,V=11=T,K=12=TBar,V=12=T,K=13=mim-modification,V=13=DELTA,K=14=mim-necessary-stimulation,V=14=CROSS_OPEN_DELTA,K=15=mim-conversion,V=15=DELTA",
                },
                "EDGE_TOOLTIP": {
                    "type": "DISCRETE",
                    "definition": "COL=ConnectorType,T=string,K=0=Elbow,V=0=Elbow,K=1=Curved,V=1=Curved,K=2=Straight,V=2=Straight",
                },
                "EDGE_UNSELECTED_PAINT": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=Color,T=string",
                },
                "EDGE_WIDTH": {
                    "type": "PASSTHROUGH",
                    "definition": "COL=LineThickness,T=double",
                },
            },
        },
    ]

    mde = {
        "name": "cyVisualProperties",
        "elementCount": len(visual_props_aspect),
        "version": "1.0",
        "consistencyGroup": 1,
        "properties": properties,
    }
    self.metadata[NiceCXNetwork.CY_VISUAL_PROPERTIES] = mde


def add_cx_node_from_gpml(self, gpml_node):
    graph_id = gpml_node.get("GraphId")
    cx_node = self.create_node(node_name=graph_id)
    entities_by_id[graph_id] = cx_node
    for name, value in sorted(gpml_node.items()):
        self.add_node_attribute(property_of=cx_node, name=name, values=value)


def add_anchors(self, gpml_edge):
    for graphics in gpml_edge.findall("ns3:Graphics", NAMESPACES):
        for anchor in graphics.findall("ns3:Anchor", NAMESPACES):
            add_cx_node_from_gpml(self, anchor)


def add_cx_edge_from_gpml(self, gpml_edge):
    # graph_id = gpml_edge.get("GraphId")
    # edge_attributes = dict()
    for graphics in gpml_edge.findall("ns3:Graphics", NAMESPACES):
        point_graph_ids = list()
        for point in graphics.findall("ns3:Point", NAMESPACES):
            GraphRef = point.get("GraphRef")
            point_graph_ids.append(GraphRef)

        start_end_point_graph_ids = list([point_graph_ids[0], point_graph_ids[-1]])
        start_end_points = list()
        for point_graph_id in start_end_point_graph_ids:
            point_id = point_graph_id
            if point_graph_id is None:
                dummy_entity_id = "dummy%r" % len(dummy_entities)
                dummy_entities.append(dummy_entity_id)
                cx_node = self.create_node(node_name=dummy_entity_id)
                entities_by_id[dummy_entity_id] = cx_node
                point_id = dummy_entity_id
            start_end_points.append(entities_by_id[point_id])

        cx_edge = self.create_edge(
            edge_source=start_end_points[0],
            edge_target=start_end_points[-1],
            edge_interaction="interacts-with",
        )

        for name, value in sorted(graphics.items()):
            self.add_edge_attribute(property_of=cx_edge, name=name, values=value)


for gpml_node in dom.findall("ns3:DataNode", NAMESPACES):
    add_cx_node_from_gpml(cx_network, gpml_node)

for gpml_node in dom.findall("ns3:Shape", NAMESPACES):
    add_cx_node_from_gpml(cx_network, gpml_node)

for gpml_node in dom.findall("ns3:Label", NAMESPACES):
    add_cx_node_from_gpml(cx_network, gpml_node)

for gpml_node in dom.findall("ns3:Group", NAMESPACES):
    add_cx_node_from_gpml(cx_network, gpml_node)

for gpml_edge in dom.findall("ns3:Interaction", NAMESPACES):
    add_anchors(cx_network, gpml_edge)

for gpml_edge in dom.findall("ns3:GraphicalLine", NAMESPACES):
    add_anchors(cx_network, gpml_edge)

for gpml_edge in dom.findall("ns3:Interaction", NAMESPACES):
    add_cx_edge_from_gpml(cx_network, gpml_edge)

for gpml_edge in dom.findall("ns3:GraphicalLine", NAMESPACES):
    add_cx_edge_from_gpml(cx_network, gpml_edge)

set_visual_properties_aspect(cx_network, {})

cx_network.print_summary()

mycx = cx_network.to_cx()
print(mycx)

# result = cx_network.upload_to(server='http://test.ndexbio.org', username=NDEX_USER, password=NDEX_PWD)

result = cx_network.update_to(
    server="http://test.ndexbio.org",
    username=NDEX_USER,
    password=NDEX_PWD,
    uuid="e2d755fe-8951-11e9-9bb5-0660b7976219",
)

print(result)

#    <Graphics ZOrder="12288" LineThickness="1.0" Color="ff0080">
#      <Point X="740.0" Y="170.0" GraphRef="aa684" RelX="0.0" RelY="1.0" />
#      <Point X="740.0" Y="210.0" GraphRef="cd799" RelX="0.0" RelY="-1.0" ArrowHead="Arrow" />
#      <Anchor Position="0.675" Shape="None" GraphId="b7b89" />
#      <Anchor Position="0.5" Shape="None" GraphId="fdd58" />
#    </Graphics>
