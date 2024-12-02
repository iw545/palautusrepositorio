KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        else:
            return False

    def lisaa(self, n):
        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = n
            self.alkioiden_lukumaara += 1

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lukumaara] = n
            self.alkioiden_lukumaara += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lukumaara % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.lukujono = self._luo_lista(self.alkioiden_lukumaara + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.lukujono)

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            self.alkioiden_lukumaara -= 1
            
    def kopioi_lista(self, a, b):
        b[:len(a)] = a

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lukumaara]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        c_taulu = a_taulu + b_taulu

        for i in range(0, len(c_taulu)):
            x.lisaa(c_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            if i in b_taulu:
                y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            if i not in b_taulu:
                z.lisaa(i)

        return z

    def __str__(self):
        listan_alkiot = self.lukujono[:(self.alkioiden_lukumaara-len(self.lukujono))]
        result = ', '.join(map(str, listan_alkiot))
        return "{" + result + "}"
