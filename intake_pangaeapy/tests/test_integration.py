import intake

import pytest
import textwrap


@pytest.fixture(scope="session")
def catalog_file(tmpdir_factory):
    """Prepare a single-entry catalog that points to actual data on pangaea.de."""
    catalog_str = textwrap.dedent(
        """
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
        """
    )
    catalog_filename = tmpdir_factory.mktemp("catalog").join("example_catalog.yaml")
    with open(catalog_filename, mode="w") as f:
        f.write(catalog_str)

    return catalog_filename


def test_full_load(catalog_file):
    # open catalog and ensure entry is present
    catalog = intake.open_catalog(str(catalog_file))
    assert "M85_1_bottles" in catalog

    # read dataframe and check that there's real data
    df = catalog["M85_1_bottles"].read()
    assert any(df["Event"].str.contains("M85/1_693"))
