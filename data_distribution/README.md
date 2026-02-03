# Probability Density Function Learning from Air Quality Data

## Overview
This project focuses on learning a Probability Density Function (PDF) from real-world air quality data.
Using NO₂ concentration measurements as the primary feature, the data is transformed through a roll-number-dependent nonlinear mapping.
The transformed values are then used to estimate the parameters of a Gaussian-like probability distribution using Maximum Likelihood Estimation (MLE)

## Objective
1. To model real-world NO₂ concentration data statistically
2. To apply a nonlinear transformation on the feature values
3. To estimate PDF parameters using Maximum Likelihood Estimation
4. To validate the learned distribution through visualization

## Methodology
The original NO₂ feature values x are transformed into a new variable z using a roll-number-dependent nonlinear transformation.
The transformed data z is assumed to follow a Gaussian-like probability density function.
Parameter estimation is performed using Maximum Likelihood Estimation, which determines the values that maximize the likelihood of observing the given transformed samples.

## Results
Learned Parameters-
mu =25.81266175882587 
lambda = 0.001460577420359888
c = 0.021561916251515552 

## Visualization
To evaluate the learned PDF, the following plot is generated:
1. Histogram of the transformed variable z.
2. Learned probability density function overlaid on the histogram
This comparison confirms how well the estimated distribution fits the observed data.
