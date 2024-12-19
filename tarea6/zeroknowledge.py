import itertools
import random

# Program to use the zero knowledge proof for ciphering and deciphering, the prover proves to the verifier
# that he knows the coloring of a 3 colored graoh without revealing the coloring


class Prover:
    def __init__(self, graph, colouring):
        # graph, key is edge and value is the nodes connected by the edge
        self.graph = graph
        # 3-coloring of the graph, key is the node and value is the colour
        self.coloring = colouring

    def permute(self):
        """
        Permute the colours in the graph colouring
        """

        # extract the colours from the coloring
        colours = list(set(self.coloring.values()))
        # generate all permutations of the coloours and randomly choose one
        all_colour_permutations = itertools.permutations(colours)
        new_colour_permutation = random.choice(list(all_colour_permutations))
        # make a dict of the old colour to the new colour
        old_colour_to_new_colour = {old: new for old,
                                    new in zip(colours, new_colour_permutation)}

        # change the colours of the coloring
        for key in self.coloring.keys():
            self.coloring[key] = old_colour_to_new_colour[self.coloring[key]]

        return self.coloring

    def get_nodes_colours(self, edge):
        """
        Function to return the colours of the nodes connected by the edge
        """
        return self.coloring[self.graph[edge][0]], self.coloring[self.graph[edge][1]]


class Verifier:
    def __init__(self, graph):
        self.graph = graph
        self.coloring = None

    def select_random_edge(self):
        """
        Select random edge in graph, this edge is sent to proover to get the colours of the nodes
        """
        # check if the coloring is valid
        random_edge = random.choice(list(self.graph.keys()))
        return random_edge

    def verify(self, colored_nodes):
        """
        Verify that the colours sent from the proover are different (adaycent nodes means differnt colours)
        """
        if colored_nodes[0] != colored_nodes[1]:
            return True
        return False


class ZeroKnowledge:
    def __init__(self, graph: dict, colouring: dict):   
        self.prover = Prover(graph, colouring)
        self.verifier = Verifier(graph)
        self.graph = graph

    def run(self):
        """
        Run the zero knowledge proof.
        Step 1: Prover permutes the colours of the graph    
        Step 2: Verifier selects a random edge and asks for the colours of the nodes
        Step 3: Prover sends the colours of the nodes
        Step 4: Verifier verifies that the colours are different
        """
        
        # run the proof for m^2 times ( m is number of edges in the graph)
        for _ in range(len(self.graph.keys())**2):

            self.prover.permute()
            random_edge = self.verifier.select_random_edge()
            coloured_nodes = self.prover.get_nodes_colours(random_edge)
            result = self.verifier.verify(coloured_nodes)
            if not result:
                print("The prover does not know the coloring")
                print(f"Colours of the nodes connected by the edge {random_edge} are {coloured_nodes}")
                return False
        print("The proover knows the colouring")
        return True





scenario = 1

if scenario == 1:
    # Simple scenario, triangle with 3 nodes and 3 colours
    zk = ZeroKnowledge(graph={1:[1,2], 2:[2,3], 3:[1,3]}, colouring={1:1, 2:2, 3:3})
elif scenario == 2:
    # Successfull scenario of 3 colouring of Pettersen graph
    zk = ZeroKnowledge(graph={1: [1, 2], 2: [2, 3], 3: [3, 4], 4: [4, 5], 5: [1, 5], 6: [1, 6],
                            7: [2, 7], 8: [3, 8], 9: [4, 9], 10: [5, 10], 11: [6, 8], 12: [6, 9],
                            13: [7, 10], 14: [7, 9], 15: [8, 10]}, colouring={1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 1, 10: 1})
elif scenario == 3:
    # Failing case, adaycent nodes 3 and 8 have the same colouring
    zk = ZeroKnowledge(graph={1: [1, 2], 2: [2, 3], 3: [3, 4], 4: [4, 5], 5: [1, 5], 6: [1, 6],
                              7: [2, 7], 8: [3, 8], 9: [4, 9], 10: [5, 10], 11: [6, 8], 12: [6, 9],
                              13: [7, 10], 14: [7, 9], 15: [8, 10]}, colouring={1: 1, 2: 2, 3: 3, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 1, 10: 1})

zk.run()
