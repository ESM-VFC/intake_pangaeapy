#!/usr/bin/env python

import intake

meteor_cat = intake.open_catalog("meteor_cruises.yaml")
print(f"Entries in {meteor_cat.name}:")
print(list(meteor_cat))

m85_1_bottles_df = meteor_cat["M85_1_bottles"].read()
print(m85_1_bottles)
