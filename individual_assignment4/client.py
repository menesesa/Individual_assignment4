# -*- coding: utf-8 -*-

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

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": ["f", "g"],
    "f": ["h"],
    "g": ["h"],
    "h": []
     }


import requests

url = "http://127.0.0.1:5000/{}"

def upload_graph(graph): 
    data=graph
    request=requests.post(url.format("upload_graph"), json=data)
    return request.json()

def degrees_of_separation(beginning,end,graph): 
    data=graph
    request=requests.put("http://127.0.0.1:5000/degrees_of_separation/{}/{}".format(beginning,end), json=data)
    return request.json()

