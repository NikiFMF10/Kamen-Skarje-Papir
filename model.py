import random

class Igra:

    def __init__(self):
        self.izbira_racunalnika = ''
        self.izbira = ['Kamen', 'Škarje', 'Papir']


    def kaj_izbere_racunalnik (self):
        self.izbira_racunalnika = self.izbira[random.randint(0,2)]
        return self.izbira_racunalnika


    def igralec (self, izbira, racunalnik):
        if izbira == 'Kamen' and racunalnik == 'Škarje':
            return ('Zmagal si!')
        elif izbira == 'Papir' and racunalnik == 'Kamen':
            return  ('Zmagal si!')
        elif izbira == 'Škarje' and racunalnik == 'Papir':
            return ('Zmagal si!')
        elif izbira == 'Škarje' and racunalnik == 'Kamen':
            return ('Izgubil si. Poskusi ponovno!')
        elif izbira == 'Kamen' and racunalnik == 'Papir':
            return ('Izgubil si. Poskusi ponovno!')
        elif izbira == 'Papir' and racunalnik == 'Škarje':
            return ('Izgubil si. Poskusi ponovno!')
        else:
            return ('Neodločeno. Naslednja igra je tvoja!')
    
    
    def racunalnik_izbere():
        rac = Igra.kaj_izbere_racunalnik()
        return rac


    def zmagovalec (izbira, racunalnik):
        zmag = Igra.igralec(izbira, racunalnik)
        return zmag


    def stevilo_zmag (self, izbira, racunalnik):
        udelezenec = Igra.igralec(izbira, racunalnik)
        if udelezenec == 'Zmagal si!':
            self.stevilo_zmag_igralca += 1
        elif udelezenec == 'Izgubil si. Poskusi ponovno!':
            self.stevilo_zmag_racunalnika += 1
        else:
            self.stevilo_zmag_igralca += 0
            self.stevilo_zmag_racunalnika += 0


        self.tekst1.config(tekst = 'Igralec je zmagal' + str(self.stevilo_zmag_igralca) + 'krat.')
        self.tekst2.config(tekst = 'Računalnik je zmagal' + str(self.stevilo_zmag_racunalnika) + 'krat.')


def nova_igra():
    return Igra()


ZACETEK = 'Z'
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