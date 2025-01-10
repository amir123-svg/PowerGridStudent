import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        terrain = Terrain()
        ##terrain.charger("test_terrain.txt")

        self.assertEqual(terrain.largeur, 4)
        self.assertEqual(terrain.hauteur, 3)

        self.assertEqual(terrain.cases[0][0], Case.ENTREE)
        
        self.assertEqual(terrain.cases[0][1], Case.VIDE)
        self.assertEqual(terrain.cases[1][1], Case.VIDE)
        self.assertEqual(terrain.cases[1][2], Case.VIDE)
        self.assertEqual(terrain.cases[1][3], Case.VIDE)
        self.assertEqual(terrain.cases[1][5], Case.VIDE)
        self.assertEqual(terrain.cases[2][1], Case.VIDE)
        self.assertEqual(terrain.cases[2][2], Case.VIDE)
        self.assertEqual(terrain.cases[2][3], Case.VIDE)
        self.assertEqual(terrain.cases[2][4], Case.VIDE)
        self.assertEqual(terrain.cases[2][5], Case.VIDE)
        self.assertEqual(terrain.cases[3][4], Case.VIDE)
        self.assertEqual(terrain.cases[4][0], Case.VIDE)
        self.assertEqual(terrain.cases[4][3], Case.VIDE)
        self.assertEqual(terrain.cases[4][4], Case.VIDE)
        self.assertEqual(terrain.cases[5][0], Case.VIDE)
        self.assertEqual(terrain.cases[5][2], Case.VIDE)
        self.assertEqual(terrain.cases[5][3], Case.VIDE)
        self.assertEqual(terrain.cases[5][5], Case.VIDE)
        
        self.assertEqual(terrain.cases[0][5], Case.CLIENT)
        self.assertEqual(terrain.cases[1][0], Case.CLIENT)
        self.assertEqual(terrain.cases[2][0], Case.CLIENT)
        self.assertEqual(terrain.cases[4][5], Case.CLIENT)
        self.assertEqual(terrain.cases[5][1], Case.CLIENT)
        self.assertEqual(terrain.cases[5][4], Case.CLIENT)
        
        self.assertEqual(terrain.cases[0][2], Case.OBSTACLE)
        self.assertEqual(terrain.cases[0][3], Case.OBSTACLE)
        self.assertEqual(terrain.cases[0][4], Case.OBSTACLE)
        self.assertEqual(terrain.cases[1][4], Case.OBSTACLE)
        self.assertEqual(terrain.cases[3][0], Case.OBSTACLE)
        self.assertEqual(terrain.cases[3][1], Case.OBSTACLE)
        self.assertEqual(terrain.cases[3][2], Case.OBSTACLE)
        self.assertEqual(terrain.cases[3][5], Case.OBSTACLE)
        self.assertEqual(terrain.cases[4][1], Case.OBSTACLE)
        self.assertEqual(terrain.cases[4][2], Case.OBSTACLE)


    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
