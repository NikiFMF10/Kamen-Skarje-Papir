import random

class KamenSkarjePapir:

    def __init__(self):
        self.izbira_računalnika = ''
        self.izbira = ['Kamen', 'Škarje', 'Papir']

    def kaj_izbere_računalnik (self):
        self.kaj_izbere_računalnik = self.izbira[random.randit(0,2)]
        return self.kaj_izbere_računalnik

    def igralec (self, izbira, računalnik):
        if izbira == 'Kamen' and računalnik == 'Škarje':
            return ('Zmagal si!')
        elif izbira == 'Papir' and računalnik == 'Kamen':
            return  ('Zmagal si!')
        elif izbira == 'Škarje' and računalnik == 'Papir':
            return ('Zmagal si!')
        elif izbira == 'Škarje' and računalnik == 'Kamen':
            return ('Izgubil si. Poskusi ponovno!')
        elif izbira == 'Kamen' and računalnik == 'Papir':
            return ('Izgubil si. Poskusi ponovno!')
        elif izbira == 'Papir' and računalnik == 'Škarje':
            return ('Izgubil si. Poskusi ponovno!')
        else:
            return ('Neodločeno. Naslednja igra je tvoja!')
