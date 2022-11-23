"""
This script adds GoodReads url to the dataset
"""

import pandas as pd
import yaml
from yaml.loader import SafeLoader

config_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4125 - Developing Data Products\Assignments\Team Assignment - book recommendation\code\config.yaml"

def get_goodreads_search_path(isbn):
    goodreads_search_url_path = f"https://www.goodreads.com/search?utf8=%E2%9C%93&query={isbn}"
    return goodreads_search_url_path

if __name__ == "__main__":

    # read config file - where the data path is found
    with open(config_path) as f:
        config = yaml.load(f, Loader=SafeLoader)

    # add GoodReads url - the Kaggle dataset does not contain goodreads url of the book
    book = pd.read_csv(config['raw_data_path_book'], low_memory=False)
    book['url'] = book['ISBN'].map(get_goodreads_search_path)
    
    # save
    book.to_csv(config['raw_data_path_book'], index = False)