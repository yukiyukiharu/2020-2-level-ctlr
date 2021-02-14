"""
Checks raw dataset volume
"""

import os
import unittest
from constants import ASSETS_PATH


class VolumeCHeckTest(unittest.TestCase):
    """
    Checks folder volume is appropriate
    """
    def test_folder_is_appropriate(self):
        self.assertTrue(os.listdir(ASSETS_PATH),
                        msg="ASSETS_PATH directory is empty")
