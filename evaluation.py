"""
Evaluation functions for recommender model
"""
from random import sample
from tqdm import tqdm

# evaluate model over n samples from test set 
def evaluate(model, test_set, n = 1000, num_rec = 20):
    total_recall = 0 
    test_users = sample(test_set['User-ID'].unique().tolist(), n)
    for user_id in tqdm(test_users):
        ground_truth_item_ids = test_set.loc[test_set['User-ID']==user_id,"ISBN"].values.tolist()
        total_recall += evaluate_user(model, user_id, ground_truth_item_ids, num_rec)
    return total_recall/n
   
# evaluate model on 1 user
def evaluate_user(model, user_id, ground_truth_item_ids, num_rec = 20):
    # recommend items
    recommended_item_ids = model.recommend(user_id, num_rec)
    # compute metric 
    recall = compute_recall(ground_truth_item_ids, recommended_item_ids)
    return recall

# compute recall - fraction of recommended items that were relevant
def compute_recall(actual_items, predicted_items):
    actual_set = set(actual_items)
    predicted_set = set(predicted_items)
    return len(actual_set & predicted_set)/len(actual_set)