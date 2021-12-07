import pandas as pd
import numpy as np

input1 = [
    199
    ,200
    ,208
    ,210
    ,200
    ,207
    ,240
    ,269
    ,260
    ,263
]

file_path = 'day_1_input.txt'

def read_txt(file_path):
    with open(file_path) as file:
        data = file.readlines()
        data = map(lambda x: int(x.replace('\n','')), data)
    return data

def main(input):
    """Calculate number of increased values"""
    df = pd.DataFrame(input,columns=['values'])
    df['lag'] = df['values'].shift(1)
    df['is_increased'] = np.where(df['values'] > df['lag'], True, False)
    print(df.dtypes)

    increased_no = df['is_increased'].sum()
    print(increased_no)


data = read_txt(file_path)
main(data)