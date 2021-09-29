import os

from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    df['fixed acidity'].fillna(int(df['fixed acidity'].median()), inplace=True)
    df['volatile acidity'].fillna(int(df['volatile acidity'].mean()), inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    replace_map = {'type': {'white': 1, 'red': 2}}
    types = df['type'].astype('category').cat.categories.tolist()
    replace_map_comp = {'type': {k: v for k, v in zip(types, list(range(1, len(types) + 1)))}}
    df.replace(replace_map_comp, inplace=True)
    print(df.head())
    raw_data_path = config['load_data']['raw_dataset_csv']

    df.to_csv(raw_data_path, sep = ',', index = False, header = new_cols)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(parsed_args.config)