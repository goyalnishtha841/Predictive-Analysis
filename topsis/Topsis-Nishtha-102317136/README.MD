# TOPSIS – Technique for Order Preference by Similarity to Ideal Solution

A lightweight Python package implementing the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making (MCDM).

This package allows users to rank alternatives based on multiple weighted criteria directly from the command line.

## Installation

Install the package using pip:

pip install Topsis-Nishtha-102317136

## Command Line Usage

After installation, run:

topsis <InputFile> <Weights> <Impacts> <OutputFile>

### Example
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv

## Input File Format

The input file must contain:

- First column → Alternative names (non-numeric)
- Remaining columns → Numeric criteria values

## Input Validation Rules

- Minimum 3 columns required
- First column must be non-numeric
- Remaining columns must be numeric
- Number of weights = number of impacts
- Impacts must be `+` or `-`

### Example (`data.csv`)

| Fund | P1 | P2 | P3 | P4 |
|------|----|----|----|----|
| M1 | 0.67 | 0.45 | 6.5 | 42.6 |
| M2 | 0.60 | 0.36 | 3.6 | 53.3 |
| M3 | 0.82 | 0.67 | 3.8 | 63.1 |

## Weights

Weights represent the **importance** of each criterion.

### Example 
"1,1,1,2"

Meaning:
- Criterion 4 is twice as important

## Impacts

Impacts indicate whether higher values are beneficial or costly.

| Symbol | Meaning |
|--------|---------|
| + | Benefit criterion (higher is better) |
| - | Cost criterion (lower is better) |

### Example:
"+,+,-,+"

## Output

### The output file is saved as a CSV containing two additional columns:

Topsis Score – Relative performance score
Rank – Ranking of alternatives (1 = best)

## Methodology

TOPSIS ranks alternatives by:
Normalizing the decision matrix
Applying weights
Determining ideal best and worst solutions
Calculating Euclidean distances
Computing similarity scores
Assigning ranks

## Author

Nishtha Goyal
