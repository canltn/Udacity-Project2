import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://canltncosmosmgdb:I4hiCFq7cMR1OomtZWapFOdFKmulj7mu1Y5YEuDpzg2mIJ8FHAlAtSoOL012A5zgrd1es1R9ytlaACDbS74OYA%3D%3D@canltncosmosmgdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@canltncosmosmgdb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            db_name ="canltn-db"
            database = client[db_name]
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
