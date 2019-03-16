# CPE 203 Project 5
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 3/12/2019
#
# Project 5
# Section 5
# Purpose of Project: Find connected components and testing if graph is bipartite
# additional comments

from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = 'black'

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        #create graph
        self.ashleys_dictionary = {}
        self.graph = self.create_graph(filename)

    def create_graph(self, filename):
        #read file and create a list of vertices
        try:
            f = open(filename)
            for line in f:
                [v1, v2] = line.split()
                #Create nodes
                self.add_vertex(v1)
                self.add_vertex(v2)
                #add to a-list
                self.add_edge(v1, v2)
            f.close()
        except FileNotFoundError as e:
            print(e)
            exit()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        #check if vertex is already in graph
        if key not in self.ashleys_dictionary:
            self.ashleys_dictionary[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.get_vertices():
            return self.ashleys_dictionary[key] 
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.ashleys_dictionary[v2].adjacent_to.append(v1)
        self.ashleys_dictionary[v1].adjacent_to.append(v2)
        #does not account for if vertex is already in a-list

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        ordered_vertices = []
        for vertex in self.ashleys_dictionary:
            ordered_vertices.append(self.ashleys_dictionary[vertex].id)
        return sorted(ordered_vertices)

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        results = []
        visited_vertices = []
        vertices = self.get_vertices()
        stack = Stack(len(vertices))
        for vertex in vertices:
            temp_results = []
            if vertex not in visited_vertices:
                stack.push(vertex)
            while not stack.is_empty():
                vertex = stack.pop()  
                if vertex not in visited_vertices:
                    visited_vertices.append(vertex)
                    temp_results.append(vertex)
                    for avertex in self.get_vertex(vertex).adjacent_to:
                        if avertex not in temp_results and avertex not in visited_vertices:
                            stack.push(avertex)
            if len(temp_results) != 0:
                results.append(sorted(temp_results))
        return sorted(results, key=lambda result: result[0])

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        graphs = self.conn_components()
        for graph in graphs:
            visited_vertices = []
            queue = Queue(len(graph))
            queue.enqueue(graph[0])
            while not queue.is_empty():
                vertex = queue.dequeue()
                if vertex not in visited_vertices:
                    v1_color = self.get_vertex(vertex).color
                    visited_vertices.append(vertex)
                    for avertex in self.get_vertex(vertex).adjacent_to:
                        if v1_color == 'black':
                            self.get_vertex(avertex).color = 'red'
                        v2_color = self.get_vertex(avertex).color
                        if v1_color == v2_color:
                            return False
                        if avertex not in visited_vertices:
                            queue.enqueue(avertex)
        return True
