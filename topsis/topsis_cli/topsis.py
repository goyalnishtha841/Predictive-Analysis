import sys
import pandas as pd
import numpy as np


def validate_inputs(df, weights, impacts):

    # minimum columns
    if df.shape[1] < 3:
        raise Exception("Input file must contain three or more columns.")

    # numeric check (2nd to last columns)
    try:
        df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
    except:
        raise Exception("Columns from 2nd to last must contain numeric values only.")

    # length checks
    if len(weights) != len(impacts):
        raise Exception("Number of weights and impacts must be same.")

    if len(weights) != df.shape[1] - 1:
        raise Exception("Weights/Impacts count must match number of criteria columns.")

    # impact validation
    for i in impacts:
        if i not in ['+', '-']:
            raise Exception("Impacts must be either + or -.")


def topsis(df, weights, impacts):

    data = df.iloc[:, 1:].values.astype(float)

    # Step 1: Normalization
    norm = data / np.sqrt((data ** 2).sum(axis=0))

    # Step 2: Weighted normalized matrix
    weights = np.array(weights)
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(np.max(weighted[:, i]))
            ideal_worst.append(np.min(weighted[:, i]))
        else:
            ideal_best.append(np.min(weighted[:, i]))
            ideal_worst.append(np.max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance calculation
    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = s_minus / (s_plus + s_minus)

    # Step 6: Ranking
    rank = score.argsort()[::-1] + 1

    df['Topsis Score'] = score
    df['Rank'] = rank

    return df


def main():

    # parameter check
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    # parse weights & impacts
    weights = weights.split(',')
    impacts = impacts.split(',')

    try:
        weights = [float(w) for w in weights]
    except:
        print("Weights must be numeric.")
        sys.exit(1)

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    try:
        validate_inputs(df, weights, impacts)
        result = topsis(df, weights, impacts)
        result.to_csv(output_file, index=False)
        print("TOPSIS successfully applied. Output saved.")

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
