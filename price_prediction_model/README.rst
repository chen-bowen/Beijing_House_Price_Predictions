
price_prediction_model
======================

End to end lightGBM regression model to predict house prices in Beijing

Project Organization
--------------------

.. code-block::

   │
   ├── data/               <- The original, immutable data dump. 
   │
   ├── figures/            <- Figures saved by scripts or notebooks.
   │
   ├── notebooks/          <- Jupyter notebooks. Naming convention is a short `-` delimited 
   │                         description, a number (for ordering), and the creator's initials,
   │                        e.g. `initial-data-exploration-01-hg`.
   │
   ├── output/             <- Manipulated data, logs, etc.
   │
   ├── tests/              <- Unit tests.
   │
   ├── price_prediction_model/      <- Python module with source code of this project.
   │
   ├── environment.yml     <- conda virtual environment definition file.
   │
   ├── LICENSE
   │
   ├── Makefile            <- Makefile with commands like `make environment`
   │
   ├── README.md           <- The top-level README for developers using this project.
   │
   └── tox.ini             <- tox file with settings for running tox; see tox.testrun.org



----


.. raw:: html

   <p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</p>


Set up
------

Install the virtual environment with conda and activate it:

.. code-block:: bash

   $ conda env create -f environment.yml
   $ conda activate example-project

Install ``price_prediction_model`` in the virtual environment:

.. code-block:: bash

   $ pip install --editable .
