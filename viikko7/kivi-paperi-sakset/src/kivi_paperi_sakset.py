from tuomari import Tuomari
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

class KiviPaperiSakset:
    def pelaa(self, vastaus):
        tuomari = Tuomari()

        self._peli = luo_peli(vastaus)
        if vastaus == "a":
            tekoaly = 0
        else:
            tekoaly = 1

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto, tekoaly)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto, tekoaly)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto, tekoaly):
        if tekoaly == 0:
            return self._peli.pelaa()
        else:
            return self._peli.pelaa(ensimmaisen_siirto)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
def luo_peli(vastaus):
    if vastaus == "a":
        peli = KPSPelaajaVsPelaaja()
    elif vastaus == "b":
        peli = KPSTekoaly
    elif vastaus == "c":
        peli = KPSParempiTekoaly

    return peli
