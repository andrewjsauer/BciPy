import os
import sys
sys.path.append('.')
import unittest
from bcipy.language_model.language_model import LangModel
from bcipy.language_model.lm_modes import lmtype
from bcipy.language_model.errors import NBestError, EvidenceDataStructError

# a docker mockup could have been a great idea is I had further processed the output. In the current case it's more reliable to test directly docker's output to ensure a valid output.


class TestOCLM(unittest.TestCase):

    def test_incorrect_nbest(self):
        """
        confirm an assertion error as
        the provided nbest arg is invalid
        """
        lm = lmtype('oclm')
        # init LMWrapper
        lmodel = LangModel(lm, logfile="lmwrap.log")
        nbest = 1.6
        with self.assertRaises(NBestError) as er:
            lmodel.init(nbest)

    def test_incorrect_evidence(self):
        """
        confirm the process provides
        an error given an incorrect
        input
        """
        lm = lmtype('oclm')
        # init LMWrapper
        lmodel = LangModel(lm, logfile="lmwrap.log")
        nbest = 2
        lmodel.init(nbest)
        evidence = ['t']
        return_mode = 'letter'
        # try to get priors
        with self.assertRaises(EvidenceDataStructError) as er:
            lmodel.state_update(evidence, return_mode)

    def test_valid_output(self):
        """
        confirm the process provides
        a valid output given a valid
        input
        """
        lm = lmtype('oclm')
        # init LMWrapper
        lmodel = LangModel(lm, logfile="lmwrap.log")
        nbest = 1
        lmodel.init(nbest)
        evidence = [[("A", 0.8), ("O", 0.2)]]
        return_mode = 'letter'
        # try to get priors
        priors = lmodel.state_update(evidence, return_mode)
        self.assertIsInstance(priors, dict)
        self.assertEqual(list(priors.keys())[0], 'letter')
        self.assertIsInstance(list(priors.values())[0], list)


if __name__ == '__main__':
    unittest.main()