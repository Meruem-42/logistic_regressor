import plotly.express as px
import pandas as pd
from describe import get_numerical_features
from describe import normalize_z_score
from describe import ft_mean
from describe import ft_standard_deviation


def scatter_plot(data, x_name, y_name) :
    fig = px.scatter(data, x=x_name, y=y_name, title="test")
    fig.show()

#ADD OTHER METHOD OF SIMILARITY IT IS AMBIGUOUS (CORRELATION, MEAN CLOSENESS, STD CLOSENESS, VARIANCE CLOSENESS)
#IT IS CAPTURING ONLY FEATURES MOVEMENT THAT ARE CLOSE TO EACH OTHER
def correlation_similarity(x_col, y_col) :
    mean_x_col = ft_mean(x_col)
    mean_y_col = ft_mean(y_col)
    std_x_col = ft_standard_deviation(x_col)
    std_y_col = ft_standard_deviation(y_col)
    covariance = ((x_col - mean_x_col) * (y_col - mean_y_col)).sum() / (len(x_col) - 1)
    correlation = covariance / (std_x_col * std_y_col)
    return float(correlation)

def similar_features(df) :
    similarity = correlation_similarity(df[df.columns[0]], df[df.columns[1]])
    similarity_columns = [df.columns[0], df.columns[1]]
    for i in range(len(df.columns)) :
        for j in range(i + 1, len(df.columns)) :
            corr = correlation_similarity(df[df.columns[i]], df[df.columns[j]])
            if corr > similarity :
                similarity = corr
                similarity_columns[0] = df.columns[i]
                similarity_columns[1] = df.columns[j]
    print(similarity_columns)
    print(similarity)
    return similarity_columns

def main() :
    with open("datasets/dataset_train.csv", "r") as f :
        df = pd.read_csv(f)
    df = df.dropna()
    score_columns = get_numerical_features(df)
    cols_to_keep = df.columns[score_columns]
    df = df[cols_to_keep]
    df = df.drop("Index", axis=1)
    similar_columns = similar_features(df) 
    df = df[similar_columns]
    scatter_plot(df, similar_columns[0], similar_columns[1])

if __name__ == "__main__" :
    main()