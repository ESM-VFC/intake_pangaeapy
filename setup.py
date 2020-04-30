from setuptools import setup

setup(
    name="intake_pangaeapy",
    version="0.1.0",
    description="Intake driver for pangaeapy",
    url="https://github.com/esm-vfc/intake_pangaeapy",
    author="ESM-VFC developers",
    license="MIT",
    packages=["intake_pangaeapy"],
    entry_points={"intake.drivers": ["pangaeapy = intake_pangaeapy:PangaeapySource",]},
    zip_safe=False,
)
