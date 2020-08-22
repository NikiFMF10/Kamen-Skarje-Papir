import bottle
import model


@bottle.get('/')
def index():
    return '<h1>Igra: Kamen, Škarje, Papir</h1>'

bottle.run(reloader=True, debug=True)