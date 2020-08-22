import random

class KamenSkarjePapir:

    def __init__(self):
        self.izbira_racunalnika = ''
        self.izbira = ['Kamen', 'Škarje', 'Papir']

    def kaj_izbere_racunalnik (self):
        self.kaj_izbere_racunalnik = self.izbira[random.randint(0,2)]
        return self.kaj_izbere_racunalnik

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
