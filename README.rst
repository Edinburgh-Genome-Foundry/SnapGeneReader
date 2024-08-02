SnapGene Reader
===============

.. image:: https://github.com/Edinburgh-Genome-Foundry/SnapGeneReader/actions/workflows/build.yml/badge.svg
   :target: https://github.com/Edinburgh-Genome-Foundry/SnapGeneReader/actions/workflows/build.yml
   :alt: GitHub Actions build status

.. image:: https://coveralls.io/repos/github/Edinburgh-Genome-Foundry/SnapGeneReader/badge.svg?branch=master
    :target: https://coveralls.io/github/Edinburgh-Genome-Foundry/SnapGeneReader?branch=master


SnapGene Reader is a Python library to parse Snapgene ``*.dna`` files into dictionaries or Biopython SeqRecords:

.. code:: python

  from snapgene_reader import snapgene_file_to_dict, snapgene_file_to_seqrecord

  file_path = './snap_gene_file.dna'
  dictionary = snapgene_file_to_dict(file_path)
  seqrecord = snapgene_file_to_seqrecord(file_path)

Installation
------------

Install with PIP:

.. code:: bash

    pip install snapgene_reader

Test with Pytest:

.. code:: bash

    pytest --cov=snapgene_reader tests/


Licence = MIT
-------------

SnapGene Reader is an open-source software originally written by `Isaac Luo <https://github.com/IsaacLuo>`_ at the Cai Lab. This fork is released on `Github <https://github.com/Edinburgh-Genome-Foundry/SnapGeneReader>`_ under the MIT licence. Everyone is welcome to contribute!
