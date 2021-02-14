"""
Changes num_article param with random number in range(2, 7)
"""

import json
import random
from test_params import PARENT_CONFIG


def change_volume():
    with open(PARENT_CONFIG) as f:
        reference = json.load(f)

    num_articles = random.randint(2, 7)
    reference["total_articles_to_find_and_parse"] = num_articles

    with open(PARENT_CONFIG, "w", encoding="utf-8") as f:
        json.dump(reference, f)


if __name__ == "__main__":
    change_volume()
