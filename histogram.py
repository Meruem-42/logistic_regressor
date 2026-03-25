import plotly.express as px
import pandas as pd
from describe import get_numerical_features
from describe import normalize_z_score


def histogram(data) :
    df_long = data.melt(var_name="Feature", value_name="Value")
    fig = px.histogram(df_long, x="Value", color="Feature", nbins=20, barmode="overlay", opacity=0.2)
    fig.show()
    

def main() :
    with open("datasets/dataset_train.csv", "r") as f :
        df = pd.read_csv(f)
    df = df.dropna()
    house_list = df["Hogwarts House"]
    score_columns = get_numerical_features(df)
    cols_to_keep = df.columns[score_columns]
    df = df[cols_to_keep]
    df = df.drop("Index", axis=1)
    for column in df.columns:
        df[column] = normalize_z_score(df[column])
    histogram(df)

if __name__ == "__main__" :
    main()