
import secrets


def create_user(collection, document, username_key = "User-ID"):
    if document.get("_id") is None:
        document["_id"] = document[username_key]
    collection.insert_one(document)
    
    
def add_user_interaction(collection, user_id, ISBN):
    filter_dict = {"_id":user_id}
    update_dict = {'$push': {'interactions': ISBN}}
    collection.update_one(filter_dict, update_dict, upsert = False)


def create_password(length = 15):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    password = ""
    for _ in range(length):
        password+=secrets.choice(characters)
    return password