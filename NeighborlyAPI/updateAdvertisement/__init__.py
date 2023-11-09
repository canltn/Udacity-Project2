import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = "mongodb://canltncosmosmgdb:I4hiCFq7cMR1OomtZWapFOdFKmulj7mu1Y5YEuDpzg2mIJ8FHAlAtSoOL012A5zgrd1es1R9ytlaACDbS74OYA%3D%3D@canltncosmosmgdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@canltncosmosmgdb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            db_name ="canltn-db"
            database = client[db_name]
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

