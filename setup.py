"""
setup.py
install snapgene_reader by pip
"""

from setuptools import setup, find_packages

version = {}
with open("snapgene_reader/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="snapgene_reader",
    version=version["__version__"],
    author="yishaluo",
    maintainer="EdinburghGenomeFoundry",
    description="Convert Snapgene *.dna files dict/json/biopython.",
    long_description=open("README.rst").read(),
    license="MIT",
    keywords="DNA sequence design format converter",
    packages=find_packages(),
    install_requires=["biopython", "xmltodict", "html2text"],
)
