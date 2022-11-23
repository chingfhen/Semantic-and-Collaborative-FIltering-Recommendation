
"""
Processing functions for training and evaluation 
"""


import numpy as np
from scipy import sparse
from pandas.api.types import CategoricalDtype

def df2interact_mat(df, user_col, item_col, interact_col):
    """
    Convert (user, item, interact) dataframe to sparse interaction matrix.
    REF: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.sparse.csr_matrix.html
    :param df: dataframe of (user, item, interact)
    :param user_col: (string) user_id column name
    :param item_col: (string) item_id column name
    :param interact_col: (string) interaction column name
    :return:
        interaction_sparse: (csr) interaction matrix
        users: (numpy array) user_id
        items: (numpy array) item_id
    """
    # Extract unique ids.
    users = np.array(list(np.sort(
        df[user_col].unique())))  # Get our unique users

    items = np.array(list(
        df[item_col].unique()))  # Get our unique items that were interacted with

    interactions = list(
        df[interact_col])  # All of our interactions

    # Re-code user and item index for sparse matrix.
    # Index starting from 0
    rows = df[user_col].astype(CategoricalDtype(
        categories=users)).cat.codes

    cols = df[item_col].astype(CategoricalDtype(
        categories=items)).cat.codes

    # Construct sparse matrix.
    # Get the associated column indices
    interaction_sparse = sparse.csr_matrix(
        (interactions, (rows, cols)), shape=(len(users), len(items))
    )

    return interaction_sparse, users, items

# all samples below minimum_interaction are removed
def filter_by_num_interactions(df, main_col, sub_col, minimum_interaction = 5):
    temp_df = df.groupby(main_col).count().reset_index()
    temp_df['num_interactions'] = temp_df[sub_col]
    temp_df = temp_df[[main_col, "num_interactions"]]
    df = df.merge(temp_df, on = main_col)
    df = df[df['num_interactions'] >= minimum_interaction].reset_index(drop = True)
    return df.iloc[:,:-1]

# the column contains all ones
def add_interaction_column(df):
    df['interaction'] = 1
    return df

def train_test_split(df, train_frac = 0.9, seed = 0):
    df = df.sample(frac = 1, random_state = seed)
    train_end_index = int(train_frac*len(df))
    train, test = df[:train_end_index], df[train_end_index:]
    return train, test