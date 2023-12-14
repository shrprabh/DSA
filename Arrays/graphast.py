from graphviz import Digraph

# Function to create nodes for the AST
def add_nodes_edges(tree, parent_name, graph):
    for k in tree:
        node_name = f"{k}_{tree[k]['value']}_{id(tree[k])}"  # Unique node name
        graph.node(node_name, label=f"{k}\n{tree[k]['value']}")
        graph.edge(parent_name, node_name)
        if 'children' in tree[k]:
            add_nodes_edges(tree[k]['children'], node_name, graph)

# Define the Abstract Syntax Tree structure as a set of nested dictionaries
ast = {
    'Assignment': {
        'value': '=',
        'children': {
            'Variable': {
                'value': 'variable1',
            },
            'Expression': {
                'value': 'Method Call',
                'children': {
                    'Object': {
                        'value': 'object',
                    },
                    'Method': {
                        'value': 'method',
                    },
                    'Arguments': {
                        'value': '',
                        'children': {
                            'Number': {
                                'value': '42',
                            },
                            'Operation': {
                                'value': 'Subtraction',
                                'children': {
                                    'Method Call': {
                                        'value': 'method2',
                                        'children': {
                                            'Object': {
                                                'value': 'object2',
                                            }
                                        }
                                    },
                                    'Number': {
                                        'value': '10',
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    'If Statement': {
        'value': 'if',
        'children': {
            'Condition': {
                'value': 'Method Call',
                'children': {
                    'Object': {
                        'value': 'object3',
                    },
                    'Method': {
                        'value': 'method3',
                    },
                    'Arguments': {
                        'value': 'string_literal',
                    }
                }
            },
            'Block': {
                'value': '{}',
                'children': {
                    'Return': {
                        'value': 'return',
                        'children': {
                            'Variable': {
                                'value': 'variable2',
                            }
                        }
                    }
                }
            }
        }
    },
    'Return': {
        'value': 'return',
        'children': {
            'Variable': {
                'value': 'variable3',
            }
        }
    }
}

# Create the Digraph object
dot = Digraph()
dot.node('Root', 'Root')

# Add nodes and edges for AST
add_nodes_edges(ast, 'Root', dot)

# Visualize the graph
dot.render('/Users/shreyasprabhakar/Desktop/ast_graph', view=False, format='png')

dot.render('/Users/shreyasprabhakar/Desktop/ast_graph', view=False, format='png')

'/mnt/data/ast_graph.png'
