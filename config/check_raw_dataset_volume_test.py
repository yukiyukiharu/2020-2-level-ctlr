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
        metas, raws = 0, 0
        for file in os.listdir(ASSETS_PATH):
            if file.endswith("_raw.txt"):
                raws += 1
            if file.endswith("_meta.json"):
                metas += 1

        self.assertEqual(metas, raws,
                         msg="""Collected dataset do not contain equal number of raw_articles and metas""")
