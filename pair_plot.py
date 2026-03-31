import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from describe import get_numerical_features

def pair_plot(data, dimension, color) :
    df_plot = data[list(dimension) + [color]].copy()
    sns.pairplot(df_plot, vars=dimension, hue=color, diag_kind='hist', plot_kws={'alpha': 0.6}, diag_kws={'alpha': 0.7})
    plt.show()

def main() :
    with open("datasets/dataset_train.csv", "r") as f :
        df = pd.read_csv(f)
    df = df.dropna()
    house_list = df["Hogwarts House"]
    score_columns = get_numerical_features(df)
    cols_to_keep = df.columns[score_columns]
    cols_to_keep = cols_to_keep.drop("Index")
    df = df[cols_to_keep]
    df["Hogwarts House"] = house_list
    pair_plot(df, cols_to_keep, "Hogwarts House")

if __name__ == "__main__" :
    main()