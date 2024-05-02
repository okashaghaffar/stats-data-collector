string="""By Year
Mat Inns NO Runs HS Avg BF SR 100s 50s 0s 4s
Year 2011
5 9 0 202 63 22.44 473 42.70 0 2 2 15
Year 2012
9 16 2 689 116 49.21 1474 46.74 3 3 0 89
Year 2013
8 12 1 616 119 56.00 1127 54.65 2 3 0 73
Year 2014
10 20 1 847 169 44.57 1399 60.54 4 2 2 101
Year 2015
9 15 0 640 147 42.66 1184 54.05 2 2 0 74
Year 2016
12 18 2 1215 235 75.93 2011 60.41 4 2 0 134
Year 2017
10 16 2 1059 243 75.64 1389 76.24 5 1 2 97
Year 2018
13 24 0 1322 153 55.08 2433 54.33 5 5 2 144
Year 2019
8 11 2 612 254* 68.00 967 63.28 2 2 2 78
Year 2020
3 6 0 116 74 19.33 283 40.98 0 1 0 15
Year 2021
11 19 0 536 72 28.21 1216 44.07 0 4 4 60
Year 2022
6 11 1 265 79 26.50 672 39.43 0 1 0 33
Year 2023
8 12 0 671 186 55.91 1226 54.73 2 2 0 70
Year 2024
1 2 0 58 46 29.00 70 82.85 0 0 0"""

string2="""Home Vs Away
Span Mat Inns NO Runs HS Avg BF SR 100s 50s 0s
Home
2022-2023 7 14 1 814 157 62.61 1728 47.10 3 4
Away
2018-2023 13 25 3 557 74* 25.31 1235 45.10 0 4
Neutral
2018-2018 4 7 0 197 76 28.14 441 44.67 0 1"""

import pandas as pd
def Transformation(string):
    split,cols=splitCols(string)
    dataframe=frameFormation(split,cols)
    return dataframe


def splitCols(string):
    split=string.split("\n")
    cols=split[1].split()
    cols.insert(0,split[0])
    return split,cols

def frameFormation(split,cols):
    dataframe=[]
    str_idx=2
    for i in range(str_idx,len(split)-1):
        if i%2==0:
            values=split[i+1].split()
            values.insert(0,split[i])
            dataframe.append({
                cols[j]:values[j] for j in range(len(values)-1)

            })
    df=pd.DataFrame(dataframe)
    return df


# print(Transformation(string2))
# import numpy as np
# arr= np.full(
#     (3,4),0
# )
# print(arr)

# string ="okasha"
# print(string[::-1])