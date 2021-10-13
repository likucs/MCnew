import os
import pymongo
from info import FILTER_DB_URI

myclient = pymongo.MongoClient(FILTER_DB_URI)
mydb = myclient["Cluster0"]
mycol = mydb['USERS']
chat_col = mydb['CHATS']

async def add_user(id, username, name, dcid):
    data = {
        '_id': id,
        'username' : username,
        'name' : name,
        'dc_id' : dcid
    }
    try:
        mycol.update_one({'_id': id},  {"$set": data}, upsert=True)
    except:
        pass


async def all_users():
    count = mycol.count()
    return count


async def find_user(id):
    query = mycol.find( {"_id":id})

    try:
        for file in query:
            name = file['name']
            username = file['username']
            dc_id = file['dc_id']
        return name, username, dc_id
    except:
        return None, None, None


async def get_all_users(self):
        all_users = self.col.find({})
        return all_users
#---_---------------------_---------_------------------------------


async def add_to_chats(chat_id: int):
    return chat_col.insert_one({'_id': chat_id})
    
async def del_from_chats(chat_id: int):
    return chat_col.delete_one({'_id': chat_id})
    
async def present_in_chats(chat_id : int):
    found = chat_col.find_one({'_id': chat_id})
    if found:
        return True
    else:
        return False

def chat_count():
    return chat_col.estimated_document_count()

async def get_chats():
    chat_docs = chat_col.find()
    chat_ids = []
    for doc in chat_docs:
        chat_col.append(doc['_id'])   
    return chat_ids
