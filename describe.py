import pandas as pd
import sys
import math

def get_numerical_features(data) :
    numerical_indexes = []
    for i in range(len(data.columns)) :
        if all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in data.iloc[:, i]) :
            numerical_indexes.append(i)
    return numerical_indexes

def normalize_z_score(vector) :
    clean_list = vector.dropna()
    mean_num = ft_mean(clean_list)
    std_num = ft_standard_deviation(clean_list)
    norm_vector = [(x - mean_num)/std_num for x in clean_list]
    return norm_vector

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

def ft_percentile(num_list, percentile) :
    clean_list = num_list.dropna().sort_values()
    count_num = ft_count(clean_list)
    position = percentile/100 * (count_num - 1)
    if(percentile == 100) :
        return (clean_list[count_num - 1])
    lower_id = int(position)
    lower_num = clean_list.iloc[lower_id]
    upper_id = lower_id + 1
    if upper_id >= count_num :
        return lower_num
    upper_num = clean_list.iloc[upper_id]
    rest = position - lower_id
    result_perc = lower_num + rest * (upper_num - lower_num)
    return (result_perc)

def ft_median(num_list) :
    return ft_percentile(num_list, 50)

class Describe() :
    def __init__(self, df) :
        self.df = df
 
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
            value_num = ft_percentile(self.df.iloc[:, i], 25)
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
            value_num = ft_percentile(self.df.iloc[:, i], 75)
            print("  ", f"{str(value_num)[:10]:>10}", end="")
        print()    
    
    def describe(self) :
        columns_list = self.df.columns
        numerical_features_list = get_numerical_features(self.df)
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
    print(data.describe())
    test.describe()

if __name__ == "__main__" :
    main()