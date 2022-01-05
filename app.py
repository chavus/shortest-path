from os import name
from flask import Flask, request, jsonify, send_from_directory
from lib.fastest_route import get_all_paths, get_shortest_path, get_distance
from operator import itemgetter
import json
from urllib import parse

app = Flask(__name__, static_url_path='', static_folder='frontend/build')

@app.route("/api/fastest-route")
def api_fastest_route():
    try:
        body = request.json 
        if 'matrix' not in body:
            return {'success':False, 'message': 'Matrix is required in the payload'}, 400
        get_all_paths_params = {
            'matrix': body['matrix'],
            "origin": (body['origin'][0],body['origin'][1]) if 'origin' in body else (0,0),
            "destination": (body['destination'][0],body['destination'][1]) if 'destination' in body else (len(body['matrix'][0])-1, len(body['matrix'])-1),
            "include_diagonal": body['include_diagonal'] if 'include_diagonal' in body else False
        }
        
        all_paths = get_all_paths(**get_all_paths_params)
        shortest_path = get_shortest_path(all_paths)

        return  {'success':True, 
                'number_of_paths': len(all_paths),
                'shortest_path(s)': shortest_path,
                'distance_of_shortest_paths': shortest_path[0][0] if shortest_path else [],
                **get_all_paths_params}, 200

    except Exception as err:
         print('In exception')
         return {'success':False, 
                 'message':err.__str__()}
   

@app.route("/fastest-route")
def fastest_route():
    munq = request.args.to_dict()
    matrix = json.dumps(munq)
    matrix2 = json.loads(matrix)
    body = request.json['bool']
    print(matrix2)
    return 'hello'

@app.route('/')
def home():
    return send_from_directory(app.static_folder,'index.html')

if  __name__ == "__main__":
    app.run(port=8080, debug=True)