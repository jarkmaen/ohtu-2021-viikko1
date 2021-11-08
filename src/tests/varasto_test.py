import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_korjaa_negatiivisen_tilavuuden(self):
        v = Varasto(-10, -10)

        self.assertAlmostEqual(v.tilavuus, 0)

    def test_konstruktori_korjaa_negatiivisen_saldon(self):
        v = Varasto(-10, -10)

        self.assertAlmostEqual(v.saldo, 0)

    def test_konstruktori_tayttaa_saldon_tilavuuden_mukaan(self):
        v = Varasto(5, 10)

        self.assertAlmostEqual(v.saldo, 5)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivisen_maaran_lisays_ei_muuta_saldoa(self):
        nykyinen_saldo = self.varasto.saldo

        self.varasto.lisaa_varastoon(-1)
        
        self.assertAlmostEqual(nykyinen_saldo, self.varasto.saldo)

    def test_suuri_lisays_ei_ylita_saldoa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        nykyinen_saldo = self.varasto.saldo

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(nykyinen_saldo, self.varasto.saldo)

    def test_suuri_otto_tyhjentaa_varaston_nollille(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(100), 0)

    def test_varaston_tulostus(self):
        tulos = str(self.varasto)

        self.assertAlmostEqual(tulos, "saldo = 0, vielä tilaa 10")
