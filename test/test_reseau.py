
import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        terrain = Terrain()
        terrain.ajouter_noeud(0, (3, 3))
        
        terrain.definir_entree(1)
        self.assertEqual(terrain.noeud_entree, 1)
        
     
    def test_ajout_noeud(self):
        terrain = Terrain()
        terrain.ajouter_noeud(1, (3, 4))
        terrain.ajouter_noeud(2, (2, 4))
        terrain.ajouter_noeud(3, (3, 5))
        terrain.ajouter_noeud(4, (4, 4))

        self.assertIn(1, terrain.noeuds)
        self.assertEqual(terrain.noeuds[1], (3, 4))
        self.assertEqual(terrain.noeuds[2], (2, 4))
        self.assertEqual(terrain.noeuds[3], (3, 5))
        self.assertEqual(terrain.noeuds[4], (4, 4))

    def test_ajout_arc(self):
        terrain.ajouter_arc(1, 2)
        terrain.ajouter_arc(2, 3)
        terrain.ajouter_arc(3, 1)
        
        self.assertIn((1, 2), terrain.arcs)
        self.assertIn((2, 3), terrain.arcs)
        self.assertIn((1, 3), terrain.arcs)
        
        self.assertNotIn((2, 1), terrain.arcs) 



    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

