import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti_toimii = Maksukortti(600)
        self.kortti_ei_toimi = Maksukortti(100)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassapaate_alustettu_oikeilla_arvoilla(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)
    
    def test_kateisosto_ei_toimi_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(140)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(140), 140)

    def test_kateisosto_toimii_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
    
    def test_kateisosto_ei_toimi_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(360)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_toimii)
        
        #self.assertTrue(self.kortti_toimii.ota_rahaa(240))
        self.assertEqual(str(self.kortti_toimii), "Kortilla on rahaa 3.60 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_ei_toimi_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_ei_toimi)

        self.assertFalse(self.kortti_ei_toimi.ota_rahaa(240))
        self.assertEqual(str(self.kortti_ei_toimi), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti_ei_toimi))

    def test_korttiosto_toimii_maukkaasti(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_toimii)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_toimi_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_ei_toimi)

        self.assertFalse(self.kortti_ei_toimi.ota_rahaa(240))
        self.assertEqual(str(self.kortti_ei_toimi), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti_ei_toimi))