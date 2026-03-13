import sys
from src.exception.exception import MyException
from src.logger.logger import logging 
from src.configuration.mongo_db_connection import MongoDbClint
from src.constants import DATABASE_NAME,DATA_INGESTION_COLLECTION_NAME
from typing import Optional
import pandas as pd


class proj1:

    def __init__(self):
        try:
            self.mongo_db_clinet=MongoDbClint(DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
        
    def export_data(self,collection_name:str,database_name: Optional[str] = None)->pd.DataFrame:
        try:
            logging.info("Enterd into proj1_data file")

            if database_name is None:
                collection=self.mongo_db_clinet.database[collection_name]
            else:
                collection=self.mongo_db_clinet[database_name][collection_name]

            logging.info("mongodb data read sucessfully")

            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop("_id", axis=1, inplace=True)
            return df

        except Exception as e:
            raise MyException(e,sys)
        
