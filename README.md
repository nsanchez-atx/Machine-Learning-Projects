# Machine Learning Projects

A collection of Python projects created while learning foundational concepts in machine learning, classification, prediction, and data preprocessing.

## Projects

### Perceptron Classifier

**File:** `perceptron_classifier.py`

Implements a basic perceptron classification algorithm using the included zoo dataset.

The program:

- Initializes model weights randomly
- Calculates predictions using a weighted sum and bias
- Updates weights when predictions are incorrect
- Trains over multiple epochs
- Reports classification accuracy during training

### Dataset Classification Experiment

**File:** `dataset_correlation.py`

Uses the perceptron training process to examine how successfully the selected dataset features can be used for classification.

The program trains a perceptron and reports the resulting classification accuracy.

### Housing Price Predictor

**File:** `housing_price_predictor.py`

An experimental housing-price prediction model built from scratch using data from `Housing.csv`.

The program:

- Reads housing information from a CSV file
- Converts categorical values into numerical data
- Normalizes selected input values
- Trains model weights using prediction error
- Measures model performance during training
- Accepts housing information from the user
- Produces an estimated house price

## Technologies

- Python
- pandas
- CSV data processing
- Perceptron learning
- Data preprocessing
- Basic predictive modeling

## Datasets

The repository contains datasets used by the projects, including:

- `Housing.csv`
- `zoo_data-1.csv.xls`
- `covid-19.csv.xls`

## Running the Projects

Clone the repository:

```bash
git clone https://github.com/nsanchez-atx/Machine-Learning-Projects.git
cd Machine-Learning-Projects
```

Install the required dependency:

```bash
pip install pandas
```

Run a project with Python:

```bash
python perceptron_classifier.py
```

or:

```bash
python housing_price_predictor.py
```

## Purpose

These projects were created as learning exercises to better understand how machine-learning algorithms work internally rather than relying entirely on prebuilt machine-learning models.
