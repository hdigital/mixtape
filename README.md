# mixtape

Data files for Causal Inference: The Mixtape

Contributions are very welcome. You can [read this guide](CONTRIBUTING.md) for more guidance.

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## Installation

[Install Anaconda](https://docs.anaconda.com/anaconda/install/index.html) and create a _conda_ environment

```sh
conda env create -f environment.yml

conda activate mixtape
ipython kernel install --user --name=mixtape

conda env export > environment-export.yml
```

[Install Quarto](https://quarto.org/docs/get-started/) to render Quarto documents (`*.qmd`).

## Usage

Start [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (includes Python and R) with

```sh
conda activate mixtape
jupyter lab
```

Use _mixtape_ kernel in Jupyter Lab.

Some Python scripts include [Jupyter code cells (VS Code)](https://code.visualstudio.com/docs/python/jupyter-support-py)
