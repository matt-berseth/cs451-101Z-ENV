import logging

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


def main():
    # read in the iris csv file
    logging.info("Reading 'iris.csv' ...")
    df = pd.read_csv("iris.csv")
    logging.info(f"{df.shape[0]} rows, {df.shape[1]} columns.")
    logging.info(df.describe())

    # pull out X and y
    X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
    y = df[["Species"]].values

    logging.info("Training the classifier ...")
    clf = DecisionTreeClassifier(max_depth=3)
    clf.fit(X, y)

    logging.info("Making predictions ...")
    yhat = clf.predict(X)

    n_correct = np.sum(yhat == y[:, 0])
    logging.info(f"{n_correct} correct out of {X.shape[0]}")


if __name__ == "__main__":
    main()
