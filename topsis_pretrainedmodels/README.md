# TOPSIS-Based Selection of the Best Pre-trained Model for Text Generation

## Introduction

Text generation is an important task in Natural Language Processing (NLP) where machines automatically generate meaningful human-like text. Many pre-trained transformer models are available today, but choosing the most suitable model requires evaluating multiple factors such as performance, efficiency, and computational cost.

This project applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method to identify the best pre-trained model for text generation by considering multiple evaluation criteria simultaneously.

## Objective

The main objective of this project is to:

* Compare multiple pre-trained text generation models
* Evaluate them using different performance and efficiency metrics
* Apply the TOPSIS multi-criteria decision-making method
* Rank models and select the most balanced one

## Models Compared

The following HuggingFace pre-trained models were selected for comparison:

* **GPT-2** – Baseline transformer-based text generation model
* **GPT-Neo (1.3B)** – Larger open-source generative model
* **T5-Base** – Encoder–decoder architecture suitable for generation tasks
* **BART-Large** – Strong performance in sequence generation
* **DistilGPT-2** – Lightweight and faster alternative to GPT-2

These models represent different trade-offs between performance and computational efficiency.

## Dataset

The evaluation was performed using the **WikiText-2** dataset, a widely used benchmark dataset for language modeling and text generation research.

Dataset source:

* HuggingFace Datasets Library

## Evaluation Criteria

To fairly compare the models, multiple criteria were considered:

| Criteria       | Description                      | Type                   |
| -------------- | -------------------------------- | ---------------------- |
| Perplexity     | Measures text generation quality | Cost (Lower is better) |
| Inference Time | Time required to generate text   | Cost                   |
| Model Size     | Storage requirement of model     | Cost                   |
| Memory Usage   | GPU/CPU memory consumption       | Cost                   |

### Criteria Weights

Different importance was assigned to each criterion:

* Perplexity → **0.4**
* Inference Time → **0.2**
* Model Size → **0.2**
* Memory Usage → **0.2**

## Methodology: TOPSIS

TOPSIS is a Multi-Criteria Decision Making (MCDM) technique used to rank alternatives based on their distance from an ideal solution.

### Steps followed:

1. Construct decision matrix
2. Normalize the matrix
3. Apply weights to criteria
4. Determine ideal best and ideal worst solutions
5. Compute distances from ideal solutions
6. Calculate TOPSIS score
7. Rank models based on scores

The best model is the one closest to the ideal solution and farthest from the worst solution.

## Results

After applying TOPSIS, each model received a performance score representing its overall effectiveness considering all criteria.

Higher TOPSIS score ⇒ Better overall model performance.

The ranking graph is available in the `results/` folder.

The following graph shows the TOPSIS scores obtained by each text generation model.
Higher scores indicate better overall performance considering all evaluation criteria.

### Interpretation

* **DistilGPT-2** and **GPT-2** achieved the highest TOPSIS scores, indicating a strong balance between performance and computational efficiency.
* **T5** shows moderate performance with balanced characteristics.
* **BART** and **GPT-Neo** scored lower mainly due to higher computational and memory requirements.

This visualization helps clearly compare models and supports the final ranking obtained using the TOPSIS method.

## Conclusion

The TOPSIS analysis helps in selecting a model that achieves a balance between generation quality and computational efficiency rather than optimizing only a single metric.

From the obtained rankings, the selected model demonstrates the best trade-off among performance, speed, and resource utilization for text generation tasks.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* HuggingFace Transformers
* HuggingFace Datasets

## Key Learning Outcomes

* Understanding of Multi-Criteria Decision Making (MCDM)
* Practical implementation of TOPSIS
* Comparative evaluation of NLP models
* Performance vs efficiency trade-off analysis





