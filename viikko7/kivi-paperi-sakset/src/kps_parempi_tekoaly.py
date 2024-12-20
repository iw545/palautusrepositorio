
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly:
    def pelaa(ensimmaisen_siirto):
        tekoaly = TekoalyParannettu(10)
        tokan_siirto = tekoaly.anna_siirto()
        return tokan_siirto