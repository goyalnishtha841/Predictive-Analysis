# PDF Estimation Using GAN

## Overview
This project demonstrates probability density function (PDF) estimation using a Generative Adversarial Network (GAN). A real-world environmental dataset containing NO₂ concentration values is used to train a GAN so that the generator learns the underlying data distribution.

## Dataset
Real environmental dataset with NO₂ concentration values
Missing values removed during preprocessing
Nonlinear transformation applied to increase distribution complexity

## Methodology
### Data Preprocessing
Dataset loaded using Pandas
Null values removed
Data converted to NumPy array
Nonlinear transformation applied

### GAN Architecture
#### Generator
Fully connected neural network:
Linear (1 → 32) + ReLU
Linear (32 → 32) + ReLU
Linear (32 → 1)
Input: Random noise
Output: Synthetic samples approximating the real data distribution

#### Discriminator
Fully connected classifier:
Linear (1 → 32) + ReLU
Linear (32 → 32) + ReLU
Linear (32 → 1) + Sigmoid
Output: Probability of sample being real or generated

### Training Process

- **Loss Function:** Binary Cross-Entropy  
- **Optimizer:** Adam (learning rate = 0.001)  
- **Batch Size:** 64  
- **Epochs:** 3000

#### Final Training Results

| Epoch | Discriminator Loss | Generator Loss |
|------:|-------------------:|---------------:|
| 0     | 2.0310 | 0.7549 |
| 500   | 1.3681 | 0.7527 |
| 1000  | 1.3893 | 0.6587 |
| 1500  | 1.3871 | 0.6836 |
| 2000  | 1.4039 | 0.6851 |
| 2500  | 1.3860 | 0.6897 |


## Results
Histogram comparison between real transformed data and GAN-generated samples
Strong overlap between distributions indicates successful PDF learning

## Conclusion
The GAN successfully approximates the probability density function of the transformed NO₂ dataset, demonstrating the effectiveness of GANs for distribution modeling and density estimation
