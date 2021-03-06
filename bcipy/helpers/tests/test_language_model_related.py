

import unittest

from bcipy.helpers.lang_model_related import norm_domain


class TestLanguageModelRelated(unittest.TestCase):

    def test_norm_domain(self):
        """Test conversion from negative log likelihood to prob."""
        letters = [('S', 0.25179717717251715), ('U', 1.656395297172517),
                   ('O', 4.719718077172517), ('M', 4.824790097172517),
                   ('W', 4.846891977172517), ('T', 6.100397207172517),
                   ('P', 6.8986402471725174), ('R', 7.081149197172517),
                   ('L', 7.108869167172517), ('N', 7.508945087172517),
                   ('_', 8.251687627172517), ('C', 8.670805547172517),
                   ('E', 8.820671657172516), ('B', 8.838797187172517),
                   ('A', 9.040823557172518), ('D', 9.134643177172517),
                   ('H', 9.134643177172517), ('G', 9.193730927172517),
                   ('F', 9.265835427172517), ('V', 9.374314927172517),
                   ('K', 9.569215427172518), ('I', 9.648203427172517),
                   ('Y', 10.942930827172518), ('J', 11.299606927172517),
                   ('X', 12.329225127172517), ('Z', 12.329227027172518),
                   ('Q', 13.245515427172517)]
        expected = [
            ('S', 0.7774023970322453), ('U', 0.19082561142814908),
            ('O', 0.008917692295108082), ('M', 0.008028238843581626),
            ('W', 0.00785274617485694), ('T', 0.0022419770132497793),
            ('P', 0.0010091567002187994), ('R', 0.0008408063406892647),
            ('L', 0.0008178192862913141), ('N', 0.0005481590438212282),
            ('_', 0.0002608180220954618), ('C', 0.00017152088039886618),
            ('E', 0.0001476491573050645), ('B', 0.0001449970461439091),
            ('A', 0.0001184732267906119), ('D', 0.00010786359081437584),
            ('H', 0.00010786359081437584), ('G', 0.00010167481484983796),
            ('F', 9.460167015257232e-05), ('V', 8.487636182290733e-05),
            ('K', 6.984616150492476e-05), ('I', 6.454141629213861e-05),
            ('Y', 1.7682575696535268e-05), ('J', 1.2377788678084351e-05),
            ('X', 4.420644194323101e-06), ('Z', 4.420635795107107e-06),
            ('Q', 1.7682584413941958e-06)]
        for i, pair in enumerate(norm_domain(letters)):
            self.assertEqual(expected[i][0], pair[0])
            self.assertAlmostEqual(expected[i][1], pair[1])
