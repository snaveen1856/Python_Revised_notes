"""Hirarchical inheritance
"""


class Batsman:
    def __init__(self, runs, fifties, hundreds, avg):
        self.runs = runs
        self.fifties = fifties
        self.hundreds = hundreds
        self.avg = avg

    def show(self):
        print('Runs: ', self.runs)
        print('Fifties: ', self.fifties)
        print('Hundreds: ', self.hundreds)
        print('Batsman average: ', self.avg)


class Bowler:
    def __init__(self, wickets, srate):
        self.wickets = wickets
        self.srate = srate

    def show(self):
        print('Wickets: ', self.wickets)
        print('Bowler: ', self.srate)


class Allrounder(Batsman, Bowler):
    def __init__(self, runs, fifties, hundreds, avg, wickets, srate):
        Batsman.__init__(self, runs, fifties, hundreds, avg)
        Bowler.__init__(self, wickets, srate)

    def show(self):
        Batsman.show(self)
        Bowler.show(self)


kapil = Allrounder(4500, 45, 12, 50.5, 510, 25)
Allrounder.show(kapil)
print('-' * 40)
virat = Batsman(8564, 50, 45, 60.8)
Batsman.show(virat)
print('-' * 40)
Bombra = Bowler(560, 25)
Bowler.show(Bombra)
