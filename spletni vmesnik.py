import bottle
import model

def racunalnik_izbere():
    igra = model.KamenSkarjePapir()
    rac = igra.kaj_izbere_racunalnik()
    return rac

def zmagovalec (izbira, racunalnik):
    igra = model.KamenSkarjePapir()
    zmag = igra.igralec(izbira, racunalnik)
    return zmag

def stevilo_zmag (self, izbira, racunalnik):
    igra = model.KamenSkarjePapir()
    udelezenec = igra.igralec(izbira, racunalnik)
    if udelezenec == 'Zmagal si!':
        self.stevilo_zmag_igralca += 1
    elif udelezenec == 'Izgubil si. Poskusi ponovno!':
        self.stevilo_zmag_racunalnika += 1
    else:
        self.stevilo_zmag_igralca += 0
        self.stevilo_zmag_racunalnika += 0


@bottle.get('/')
def index():
    return '<h1>Igra: Kamen, Škarje, Papir</h1>'

bottle.run(reloader=True, debug=True)