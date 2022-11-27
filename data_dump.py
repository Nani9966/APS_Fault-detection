import pymongo
import pandas as pd
import json
client=pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="APS"
COLLECTION_NAME="SENSOR"

if __name__ =="__main__":
    df=pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
    print(f"Rows and columns:{df.shape}")

    ##convert dataframe to json so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
