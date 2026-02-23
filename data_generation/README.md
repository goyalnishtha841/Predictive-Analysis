# Data Generation using Modelling and Simulation for Machine Learning

## Introduction

Real-world datasets are not always available or may be expensive to collect. Modelling and simulation techniques allow us to generate synthetic data by controlling system parameters and observing outcomes. This project demonstrates how simulation can be used to generate large datasets and evaluate the performance of multiple machine learning models.

The goal of this assignment is to simulate data generation, perform multiple experiments, and identify the best-performing machine learning model based on evaluation metrics.

## Objective

The objectives of this project are:

* Select a simulation tool for data generation
* Study important simulation parameters and their ranges
* Generate random parameter values
* Perform 1000 simulations to create synthetic data
* Train multiple machine learning models
* Compare model performance using evaluation metrics
* Identify the best-performing model

## Simulation Tool

The simulation was implemented using **Scikit-learn Synthetic Data Generator** (`sklearn.datasets`).

This library allows controlled generation of artificial datasets by defining statistical parameters such as sample size, noise level, and number of features.

### Why this tool?

* Easy parameter control
* Fast execution
* Suitable for machine learning experiments
* Widely used in academic research

## Simulation Parameters

The following parameters were used in the simulation process:

| Parameter          | Description                 | Range     |
| ------------------ | --------------------------- | --------- |
| Number of Samples  | Dataset size per simulation | 100 – 500 |
| Number of Features | Input variables             | 5         |
| Noise Level        | Random variation in data    | 0 – 10    |
| Simulations        | Number of runs              | 1000      |

Random values were generated within these bounds to simulate different system conditions.

## Data Generation Process

1. Random simulation parameters were generated.
2. A synthetic dataset was created using `make_regression`.
3. Each simulation produced a dataset with varying noise and sample size.
4. Results from all simulations were combined into one final dataset.

This process produced a large synthetic dataset suitable for machine learning training and evaluation.

## Machine Learning Models Compared

To ensure a comprehensive evaluation, multiple machine learning algorithms from different learning categories were selected:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* Support Vector Regressor (SVR)
* K-Nearest Neighbors (KNN)

These models represent linear, ensemble, kernel-based, and instance-based learning approaches, enabling a balanced comparison across different modelling techniques.

## Evaluation Metric

Model performance was evaluated using:

**Mean Squared Error (MSE)**

Lower MSE indicates better predictive performance.

## Results

After training and testing all models, their prediction errors were compared and visualized using a bar graph.

The comparison graph is available in the `results/` folder.

### Observations

Ridge Regression achieved the lowest MSE, indicating the best predictive performance among all evaluated models.
Linear Regression and Lasso Regression performed similarly, showing that linear models can effectively capture relationships in the simulated dataset.
Gradient Boosting produced competitive results, demonstrating strong learning capability for structured data.
Support Vector Regressor (SVR) and Random Forest showed moderate performance with slightly higher prediction errors.
K-Nearest Neighbors (KNN) had higher error compared to most models, possibly due to sensitivity to feature scaling and data distribution.
Decision Tree recorded the highest MSE, suggesting overfitting or limited generalization capability on the generated dataset.

### Interpretation

The results indicate that simpler regularized linear models performed better than more complex models for this simulated environment. This suggests that the generated data follows relatively linear relationships with controlled noise levels.

The visualization clearly supports the selection of Ridge Regression as the best-performing model for this simulation-based experiment.

## Conclusion

The simulation-based approach successfully generated synthetic data through controlled parameter variation. Among the evaluated models, the model with the lowest Mean Squared Error demonstrated the best ability to learn patterns from simulated data.

This experiment shows how modelling and simulation can be effectively used to evaluate machine learning algorithms when real datasets are unavailable.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab

## Learning Outcomes

* Understanding modelling and simulation concepts
* Synthetic data generation techniques
* Running large-scale simulations
* Comparing machine learning algorithms
* Performance evaluation using statistical metrics
