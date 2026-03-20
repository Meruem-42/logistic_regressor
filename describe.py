import pandas as pd
import sys
import math

def ft_mean(num_list) :
    clean_list = num_list.dropna()
    sum = clean_list.sum()
    return (sum/ft_count(clean_list))

def ft_count(num_list) :
    return len(num_list.dropna())

def ft_standard_deviation(num_list) :
    clean_list = num_list.dropna()
    sum_dif = 0
    mean_num = ft_mean(clean_list)
    for elem in clean_list :
        sum_dif += pow(float(elem) - mean_num, 2)
    mean_dif = sum_dif/(ft_count(clean_list) - 1)
    return math.sqrt(mean_dif)

def ft_min(num_list) :
    clean_list = num_list.dropna()
    min_num = num_list[0]
    for elem in clean_list :
        if min_num > elem :
            min_num = elem
    return min_num

def ft_max(num_list) :
    clean_list = num_list.dropna()
    max_num = num_list[0]
    for elem in clean_list :
        if max_num < elem :
            max_num = elem
    return max_num

def ft_first_percentile(num_list) :
    clean_list = num_list.dropna()
    count_num = ft_count(clean_list)
    first_pct_id = round(count_num*(1/4) - 1)
    return (clean_list[first_pct_id])

def ft_median(num_list) :
    clean_list = num_list.dropna()
    count_num = ft_count(clean_list)
    median_id = round(count_num*(2/4) - 1)
    return (clean_list[median_id])

def ft_third_percentile(num_list) :
    clean_list = num_list.dropna()
    count_num = ft_count(clean_list)
    third_pct_id = round(count_num*(3/4) - 1)
    return (clean_list[third_pct_id])


class Describe() :
    def __init__(self, df) :
        self.df = df
 
    def get_numerical_features(self) :
        numerical_indexes = []
        for i in range(len(self.df.columns)) :
            if all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in self.df.iloc[:, i]) :
                numerical_indexes.append(i)
        return numerical_indexes

    def count(self, list_feature) :
        print(f"{'Count':<10}", end="")
        y = 0
        for i in list_feature :
            count_num = ft_count(self.df.iloc[:, i])
            print("  ", f"{str(count_num)[:10]:>10}", end="")
        print()

    def mean(self, list_feature) :
        print(f"{'Mean':<10}", end="")
        for i in list_feature :
            mean_num = ft_mean(self.df.iloc[:, i])
            print("  ", f"{str(mean_num)[:10]:>10}", end="")
        print()

    def std(self, list_feature) :
        print(f"{'Std':<10}", end="")
        for i in list_feature :
            std_num = ft_standard_deviation(self.df.iloc[:, i])
            print("  ", f"{str(std_num)[:10]:>10}", end="")
        print()

    def min(self, list_feature) :
        print(f"{'Min':<10}", end="")
        for i in list_feature :
            min_num = ft_min(self.df.iloc[:, i])
            print("  ", f"{str(min_num)[:10]:>10}", end="")
        print()
    
    def max(self, list_feature) :
        print(f"{'Max':<10}", end="")
        for i in list_feature :
            max_num = ft_max(self.df.iloc[:, i])
            print("  ", f"{str(max_num)[:10]:>10}", end="")
        print() 

    def first_percentile(self, list_feature) :
        print(f"{'25%':<10}", end="")
        for i in list_feature :
            value_num = ft_first_percentile(self.df.iloc[:, i])
            print("  ", f"{str(value_num)[:10]:>10}", end="")
        print()

    def median(self, list_feature) :
        print(f"{'50%':<10}", end="")
        for i in list_feature :
            value_num = ft_median(self.df.iloc[:, i])
            print("  ", f"{str(value_num)[:10]:>10}", end="")
        print()    

    def third_percentile(self, list_feature) :
        print(f"{'75%':<10}", end="")
        for i in list_feature :
            value_num = ft_third_percentile(self.df.iloc[:, i])
            print("  ", f"{str(value_num)[:10]:>10}", end="")
        print()    
    
    def describe(self) :
        columns_list = self.df.columns
        numerical_features_list = self.get_numerical_features()
        print("          ", end="")
        for i in numerical_features_list :
            print("  ", f"{columns_list[i]:>10}", end="")
        print()
        self.count(numerical_features_list)
        self.mean(numerical_features_list)
        self.std(numerical_features_list)
        self.min(numerical_features_list)
        self.first_percentile(numerical_features_list)
        self.median(numerical_features_list)
        self.third_percentile(numerical_features_list)
        self.max(numerical_features_list)
        

def main() :
    with open(sys.argv[1]) as f :
        data = pd.read_csv(f)
    test = Describe(data)
    data.describe()
    # test.describe()

if __name__ == "__main__" :
    main()