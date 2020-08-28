import bottle
import model

model = model.KamenSkarjePapir()

@bottle.get('/')
def index():
    return bottle.template('kamškapap.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_igre = model.nova_igra()
    bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    return bottle.template('igra.tpl',
    igra = model.igre[id_igre][0],
    id_igre = id_igre,
    poskus = model.igre[id_igre][1])

@bottle.post('/igra/<id_igre:int>/')
def igralec(id_igre):
    izbira = bottle.request.forms.getunicode("beseda")
    model.igralec(id_igre, izbira)
    bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root = 'img')

bottle.run(reloader=True, debug=True)