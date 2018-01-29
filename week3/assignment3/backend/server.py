'''
This is our CRUD RESTful server. It uses the wtplugin to take care
of the database. Access to the API is provided through
http://localhost:8089/api. This URI accepts HTTP requests of the
following methods: POST, GET, DELETE, UPDATE, PUT.
The documentation of this API can be found in server.html and has
been generated with pydoc.

The db attribute required by all functions is injected by wtplugin.
It should be ignored when accessing the API.
'''

import json
from bottle import get, post, put, delete, request, route, response, abort;

@post('/api')
def post(db):
    '''
    Persists a new phone to the database. It expects data in JSON format.

    Accessable via /api through POST.
    '''
    brand = request.json['brand'];
    model = request.json['model'];
    os = request.json['os'];
    image = request.json['image'];
    screensize = request.json['screensize'];

    db.execute("""
    INSERT INTO phones
    (brand, model, os, image, screensize)
    VALUES (?, ?, ?, ?, ?);
    """, (brand,model,os,image,screensize))
    return

@get('/api')
def get_all(db):
    '''
    Returns all the elements in the database in JSON format.

    Accessable via /api through GET.
    '''
    db.execute("SELECT * FROM phones")

    response.status = 200  #OK
    response.content_type = "application\json"

    return json.dumps(db.fetchall())

@route('/api/<id>', method='GET')
def get_from_id(db, id):
    '''
    Retrieves an element from the database based on its id.

    Accessable via /api/<id> through GET. Returns a response
    in JSON format.
    Returns status 404 if the element with the specified  id hasn't been found.
    Returns status 200 otherwise.
    '''

    db.execute("SELECT * FROM phones WHERE id=?", id)

    list = db.fetchall()
    if not list:
        abort(404, "Not Found")

    response.status = 200;  #OK
    response.content_type = "application\json";
    return json.dumps(list)

@put('/api/<id>')
def put(db, id):
    '''
    Updates an element in the database based on its id. All the attributes
    should be provided via JSON including the id of the element to be updated.

    Accessable via /api/id through PUT.
    Returns status 404 if the element with the specified  id hasn't been found.
    Returns status 200 otherwise.
    '''

    db.execute("SELECT * FROM phones WHERE id=?", id)

    list = db.fetchall()
    if not list:
        abort(404, "Not Found")

    brand = request.json['brand']
    model = request.json['model']
    os = request.json['os']
    image = request.json['image']
    screensize = request.json['screensize']

    db.execute("""
      UPDATE phones
      SET brand = ?, model = ?, os = ?, image = ?, screensize = ?
      WHERE id = ?;
       """, (brand, model, os, image, screensize, id))

    response.status = 200  #OK

@delete('/api/<id>')
def delete(db,id):
    '''
    Deletes an element in the database based on its id. The id should
    be provided via JSON.

    Accessable via /api/<id> through DELETE.
    Returns status 404 if the element with the specified  id hasn't been found.
    Returns status 200 otherwise.
    '''

    db.execute("SELECT * FROM phones WHERE id=?", id)

    list = db.fetchall()
    if not list:
        abort(404, "Not Found")

    db.execute("""
    DELETE FROM phones
    WHERE id = ?
    """, id)

    response.status = 200  #OK

#TODO STATUS 404 not found -> all crud methods
#TODO insert right headers


if __name__ == "__main__":
    from bottle import install, run
    from wtplugin import WtDbPlugin, WtCorsPlugin

    install(WtDbPlugin())
    install(WtCorsPlugin())
    run(host='localhost', port=8089, reloader=True, debug=True, autojson=False)