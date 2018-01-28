import json
from bottle import get, post, patch, put, delete, request;

from bottle import route, run

#source documentation http://www.restapitutorial.com/lessons/httpmethods.html
#@route('/', method='GET')

@post('/api')
def post(db):

    brand = request.forms.get('brand');
    model = request.forms.get('model');
    os = request.forms.get('os');
    image = request.forms.get('image');
    screensize = request.forms.get('screensize');

    db.execute("""
    INSERT INTO phones
    (brand, model, os, image, screensize)
    VALUES (?, ?, ?, ?, ?);
    """, (brand,model,os,image,screensize))

    return

@get('/api')
def get(db):
    db.execute("SELECT * FROM phones")
    return json.dumps(db.fetchall())

#TODO CRUD -> UPDATE -> PATCH METHOD (incomplete resource)
@patch('/api')
def patch(db):
    return
#TODO CRUD -> UPDATE -> PUT METHOD (complete resource)
@put('/api')
def put(db):
    return
#TODO CRUD -> DELETE -> DELETE METHOD
@delete('/api')
def delete():
    return

#TODO OPTIONS

#TODO STATUS 404 not found -> all crud methods

#TODO insert right headers


if __name__ == "__main__":
    from bottle import install, run
    from wtplugin import WtDbPlugin, WtCorsPlugin

    install(WtDbPlugin())
    install(WtCorsPlugin())
    run(host='localhost', port=8089, reloader=True, debug=True, autojson=False)