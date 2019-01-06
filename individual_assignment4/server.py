# -*- coding: utf-8 -*-
#%%


# In this exercise we will create an HTTP server to which we can upload a
# graph and in which we can get the degrees of separation between two nodes
# in the graph.
# 1. Create a route in the server to which the user can upload a graph using
# JSON and using the POST http method. The JSON data should be
# passed as part of the request body, not in the URL.
# 2. Create a route to get the degrees of separation between two nodes in
# the previously uploaded graph.
# localhost:5000/degrees_of_separation/<origin>/<destination>.
# You can use any code we want from the exercises we’ve done in class
# related to graphs.

from flask import Flask, jsonify, request

server = Flask("Server Running on port 5000")   

@server.route('/upload-graph', methods=["POST"])
def upload_graph():
    body = request.get_json()
    return jsonify(body)


@server.route('/degrees-of-separation/<beginning>/<end>', methods=["PUT"])
def degrees_of_separation(beginning,end,path=[],graph=""):
   
    graph = request.get_json()  
    path = path + [beginning]
    
    
    
    if beginning == end:
        degree_of_separation = len(path) - int(2)
        if degree_of_separation == 0:
            return jsonify("Nodes are directly connected")
        else:
            return jsonify(degree_of_separation)
                       
    
    
    if beginning not in graph:
        return jsonify("The node requested is not in Graph")
    
    
    
    for node in graph[beginning]:
        if node not in path:
            newpath = degrees_of_separation(node, end, path, graph)
            if newpath is not None:
                return newpath
            
    
    return jsonify("None")

                
server.run()
