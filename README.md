# intake_pangaeapy

[`pangaeapy`](https://github.com/pangaea-data-publisher/pangaeapy) driver for [Intake](https://intake.readthedocs.io/).


## Installation

```shell
python -m pip install git+http://github.com/esm-vfc/intake_pangaeapy.git@v0.1.1
```


## Example Usage

There's an [example catalog](examples/meteor_cruises.yaml) that contains the following:
```yaml
metadata:
  version: 1

plugins:
  source:
      - module: intake_pangaeapy

sources:

  M85_1_bottles:
    driver: pangaeapy
    description: |
      Kieke, Dagmar; Steinfeldt, Reiner (2015): Physical oceanography,
      CFC-11, and CFC-12 measured on water bottle samples during METEOR
      cruise M85/1. PANGAEA, https://doi.org/10.1594/PANGAEA.854070
    args:
      pangaea_doi: "10.1594/PANGAEA.854070"

[...]
```

To load the data, run:
```python
In [1]: import intake

In [2]: meteor_cat = intake.open_catalog("meteor_cruises.yaml")

In [3]: list(meteor_cat)
Out[3]:
['M85_1_bottles',
 'M85_2_bottles',
 'M106_bottles',
 'M120_bottles',
 'M90_bottles']

In [4]: meteor_cat["M85_1_bottles"].read()
Out[4]:
          Event  Profile           Date/Time  ...  CFC-11  CFC-12  Bottle
0     M85/1_693        1 2011-06-25 15:16:00  ...     NaN     NaN       1
1     M85/1_693        1 2011-06-25 15:16:00  ...  3.0170  1.7679       2
2     M85/1_693        1 2011-06-25 15:16:00  ...     NaN     NaN       3
3     M85/1_693        1 2011-06-25 15:16:00  ...     NaN     NaN       4
4     M85/1_693        1 2011-06-25 15:16:00  ...     NaN     NaN       5
...         ...      ...                 ...  ...     ...     ...     ...
2522  M85/1_847      115 2011-07-31 17:49:00  ...  4.2927  2.3537      18
2523  M85/1_847      115 2011-07-31 17:49:00  ...  4.3060  2.3466      19
2524  M85/1_847      115 2011-07-31 17:49:00  ...  4.3286  2.3853      20
2525  M85/1_847      115 2011-07-31 17:49:00  ...  4.5231  2.5731      21
2526  M85/1_847      115 2011-07-31 17:49:00  ...  3.9061  2.2100      22

[2527 rows x 17 columns]

```


## Creating releases

Make sure to bump verion number
- [ ] in the [installation notes](#installation),
- [ ] in the [setup.py](setup.py)

Then, push to `master` and tag a realease on Github.
