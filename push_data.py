import os
import sys
import json
import certifi # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
from networksecurity.exception.exception import NetworkSecurityException # type: ignore
from networksecurity.logging.logger import logging # type: ignore
import pymongo

from dotenv import load_dotenv # type: ignore


load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")


ca = certifi.where()

class NetworkDataExtractor():
    def __init__(self, data_path: str):
        self.data_path = data_path


    def csv_to_json(self,file_path: str) -> list:
        try:
            logging.info(f"Reading CSV file from {file_path}")
            json_data = pd.read_csv(file_path).to_dict(orient='records')
            logging.info("Conversion successful")
            return json_data
        except Exception as e:
            logging.error(f"Error during conversion to JSON: {e}")
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, json_data: list, database: str, collection: str) -> int:
        try:
            logging.info(f"Connecting to MongoDB at {MONGO_DB_URL}")
            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = mongo_client[database]
            col = db[collection]
            result = col.insert_many(json_data)
            logging.info(f"Inserted {len(result.inserted_ids)} records into MongoDB")
            return len(result.inserted_ids)
        except Exception as e:
            logging.error(f"Error during MongoDB insertion: {e}")
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="Yash"
    collection="NetworkData"
    networkobj=NetworkDataExtractor(data_path=FILE_PATH)
    records=networkobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(json_data=records, database=DATABASE, collection=collection)
    print(no_of_records)