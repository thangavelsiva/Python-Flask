
from pymongo import MongoClient  #library to connect mongod
import pymongo

class CrudAPI:  
    def __init__(self, data):   
        self.client = MongoClient("mongodb://localhost:27017/")    #creating mongodb connection for every CRUD call
        database = data['database']
        collection = data['collection']
    
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
        


    def insert_data(self, data):   #for creating new data
        new_document = data['document']
        new_document.update({"_id":new_document['user_id']})
        try:
            response = self.collection.insert_one(new_document)
        except pymongo.errors.DuplicateKeyError:                     # To handle duplicate key errror
            return {"status":'Duplicate key '}
        
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def read(self):                  # for getting or read the data
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
 
    def update_data(self):      # for updating record    
        filter = self.data['filter']
        updated_data = {"$set": self.data['data_to_be_updated']}
        response = self.collection.update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete_data(self, data):   #for deleting record
        filter = data['filter']
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

