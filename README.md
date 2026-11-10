# ECG Classification for Arrhythmia Detection

Comparison of logistic regression, an RBF support vector machine, multilayer
perceptrons and one-dimensional convolutional neural networks for classifying
segmented ECG heartbeats into five AAMI classes: N, S, V, F and Q.

Developed by **Marco Bertazzoli Cova** and **Marco Fiorini** for the
EE4C12 Machine Learning for Electrical Engineering course at TU Delft.

## Results

Configurations were selected using macro F1 on the supplied validation split.
The selected SVM, MLP and CNN were then evaluated on the test split.

| Model | Validation macro F1 | Test macro F1 | Test accuracy |
| --- | ---: | ---: | ---: |
| Majority baseline | 0.181 | - | - |
| Logistic regression | 0.554 | - | - |
| RBF SVM | 0.939 | 0.935 | 0.988 |
| MLP | 0.9375 | 0.9275 | 0.9864 |
| CNN with dropout | 0.9273 | 0.9134 | 0.9854 |

The SVM uses per-beat normalization followed by PCA with 100 components.
The selected MLP and CNN use raw signals. Macro F1 is the main comparison
metric because the classes are strongly imbalanced.

See the [project report](Report.pdf) for the experimental setup, figures,
per-class results and limitations. These are results from the original
experiments, using fixed data splits and a single random seed.

## Setup

The recorded local environment uses Python 3.11. The package versions are
listed in [requirements.txt](requirements.txt).

```bash
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install the dependencies and start Jupyter from this folder:

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

## Dataset

The course-provided CSV files are **not included**. To rerun the experiments,
obtain an authorized copy and place the three original splits in `data/`:

```text
data/
    train_data.csv
    val_data.csv
    test_data.csv
```

Each file has no header. Each row contains 250 ECG samples followed by one
numeric label in the range 0-14. The notebooks map these labels to the five
AAMI classes. See [data/README.md](data/README.md) for the label mapping.

The dataset already includes beat segmentation and fixed training,
validation and test splits. A different ECG dataset or a different split
will not reproduce the reported scores.

## Notebooks

| Order | Notebook | Purpose |
| --- | --- | --- |
| 1 | [Data exploration](notebooks/EDA%20and%20NNs/data_exploration.ipynb) | Data quality, class distributions and waveform examples |
| 2 | [Logistic regression and PCA](notebooks/logreg_pca_preprocessing.ipynb) | Baseline, PCA analysis and preprocessing comparisons |
| 3 | [RBF SVM](notebooks/svm_preprocessing.ipynb) | Hyperparameter search and final evaluation |
| 4 | [Neural networks](notebooks/EDA%20and%20NNs/neural_networks.ipynb) | MLP architecture, regularization, PCA and FFT comparisons; 15-class experiment |
| 5 | [Convolutional neural networks](notebooks/EDA%20and%20NNs/convolutional_neural_network.ipynb) | CNN architecture comparisons and early stopping |

Each notebook loads its own data and can run independently. Select the
Python kernel for the environment above and run cells from top to bottom
with a fresh kernel. The working directory can be the project root or any
folder inside it. Training and grid searches can take several minutes or
longer depending on the machine.

Saved notebook outputs have been cleared. The report retains the original
results and figures; rerunning a notebook generates its outputs locally.

## Shared preprocessing

[src/data_preprocessing.py](src/data_preprocessing.py) contains the AAMI
label mapping, training-set-fitted standardization and PCA, and FFT feature
extraction. The logistic regression and SVM notebooks also implement
per-beat median subtraction and amplitude normalization.

Preprocessing is fitted on training data. The supplied validation set is
used for model selection. SVM tuning uses a stratified 20% subset of the
training split before fitting the chosen configuration on the full split.

## Report source

The LaTeX source and the figures it uses are in [report/](report/).
With a LaTeX installation containing the required packages, build from that
folder, then use the resulting `report/main.pdf`:

```bash
pdflatex main.tex
pdflatex main.tex
```

## Attribution

Course materials and library references are cited in the report.
