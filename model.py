import random

ZMAGA = 'Z'
PORAZ = 'P'


class Igra:

    def __init__(self, stevilo_zmag=0, stevilo_porazov=0):
        self.izbira_racunalnika = ''
        self.izbira = ['Kamen', 'Škarje', 'Papir']

        self.stevilo_zmag = stevilo_zmag
        self.stevilo_porazov = stevilo_porazov


    def igralec (self, izbira):
        racunalnik = self.kaj_izbere_racunalnik()

        if ((izbira == 'Kamen' and racunalnik == 'Škarje') or
        (izbira == 'Papir' and racunalnik == 'Kamen') or
        (izbira == 'Škarje' and racunalnik == 'Papir')):
            self.stevilo_zmag += 1
            return ('Zmagal si!')

        elif ((izbira == 'Škarje' and racunalnik == 'Kamen') or
        (izbira == 'Kamen' and racunalnik == 'Papir') or
        (izbira == 'Papir' and racunalnik == 'Škarje')):
            self.stevilo_porazov += 1
            return ('Izgubil si. Poskusi ponovno!')

        else:
            return ('Neodločeno. Naslednja igra je tvoja!')
    

        if self.zmaga():
            return ZMAGA

        if self.poraz():
            return PORAZ


    def kaj_izbere_racunalnik(self):
        self.izbira_racunalnika = self.izbira[random.randint(0,2)]
        return self.izbira_racunalnika
        print (self.izbira_racunalnika)

    
    def zmaga(self):
        if self.stevilo_zmag == 3:
            return True
        else:
            return False

    
    def poraz(self):
        if self.stevilo_porazov == 3:
            return True
        else:
            return False

    
    def koliko_zmag(self, izbira):
        return self.stevilo_zmag

    def koliko_porazov(self, izbira):
        return self.stevilo_porazov
    

    #def zmagovalec (izbira, racunalnik):
        #zmag = Igra.igralec(izbira, racunalnik)
        #return zmag


        #self.tekst1.config(tekst = 'Igralec je zmagal' + str(self.stevilo_zmag) + 'krat.')
        #self.tekst2.config(tekst = 'Računalnik je zmagal' + str(self.stevilo_porazov) + 'krat.')


def nova_igra():
    return Igra()

Igra().igralec('Škarje')


ZACETEK = 'A'
class KamenSkarjePapir:
    
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def igralec(self, id_igre, izbira):
        igra = self.igre[id_igre][0]
        novo_stanje = igra.igralec(izbira)
        self.igre[id_igre] = (igra, novo_stanje)    