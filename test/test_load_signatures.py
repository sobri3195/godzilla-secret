import unittest

import yaml

from godzilla.__main__ import SignatureRecognizer
from godzilla.defaults import DEFAULT_CONFIG_PATH


class SignatureLoadTest(unittest.TestCase):

    def test_load_default_config(self):
        """ Test to ensure default config is valid. """
        with open(DEFAULT_CONFIG_PATH) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            signatures = SignatureRecognizer.load_signatures(config['signatures'], [])
            self.assertTrue(len(signatures) > 0)
