# tstrait paper

This directory includes the Jupyter notebook files to generate the figure used in the tstrait paper.

## Preliminary Information

### Requirements:

The required packages to run the Jupyter notebook file are stated in `requirements/requirements.txt` (See [here](requirements/requirements.txt)). Please install them before running the codes.

Please see

- [tstrait installation](https://tskit.dev/tstrait/docs/stable/install.html)
- [tskit installation](https://tskit.dev/tskit/docs/stable/installation.html)

for details on installing the packages.

### Comparison

We compare `tstrait` with the simulation algorithm described in [Martin et al. (2017)](https://www.sciencedirect.com/science/article/pii/S0002929717301076). The codes in `genotype_matrix.py` is adapted from the `true_prs` function in https://github.com/armartin/ancestry_pipeline/blob/master/simulate_prs.py#L111, and it is used as a simulation framework described in Martin et al. (2017).

### Data

We use the French Canadian and the 1000 Genomes Project to examine the simulation time. Chromosome 9 is used for both datasets, and they can be installed from:

- French Canadian dataset (`simulated_genomes_chr9.tsz`): https://zenodo.org/record/6839683
- 1000 Genomes Project (`1kg_chr9.trees.tsz`): https://zenodo.org/record/3051855

### Simulation Time

The simulation time data is stored in `output` folder. The times reported are the total CPU time required to simulate quantitative traits on an Intel(R) Core(TM) i9-11900H CPU and 16 GB of RAM.

## Jupyter Notebook

We now describe the Jupyter notebooks that are used to measure the simulation time. Please use the notebooks in the following order:

1. `tree-sequence-save.ipynb`

This notebook simulates large sample tree sequences from `stdpopsim` and saves them in the `data` folder. Please run this notebook overnight, as it will take an extremely long time to finish the simulations.

2. `time-num-individual.ipynb`

This notebook uses the tree sequences that are simulated in `tree-sequence-save.ipynb` to examine how the number of individuals is influencing the simulation speed.

3. `French-Canadian-Size.ipynb`

This notebook examines the computational size of the French Canadian dataset.

4. `time-num-causal.ipynb`

This notebook uses the French Canadian dataset and the inferred tree sequence from the 1000 Genomes Project to examine how the number of causal sites is influencing the simulation speed. Please run this notebook overnight, as it will take an extremely long time to finish the simulations.

5. `figure.ipynb`

This notebook creates the figure of `tstrait`'s simulation time by using the output of `time-num-individual.ipynb` and `time-num-causal.ipynb`.