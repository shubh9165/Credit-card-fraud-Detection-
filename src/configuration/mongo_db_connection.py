import os
import pymongo
from src.constants import DATABASE_NAME,MONGODB_URL_KEY
from src.exception import MyException
from src.logger import logging
import sys


class MongoDbClint:

    clinet=None

    def __init__(self,DATABASE_NAME):
        try:
            logging.info("Mongodb Connection process are getting start")
            if MongoDbClint.clinet is None:
                mongo_db_url=os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
            
                MongoDbClint.clinet=pymongo.MongoClient(mongo_db_url)
                logging.info("Mongodb data base read sucessfully")

            self.clinet=MongoDbClint.clinet
            self.database=self.clinet[DATABASE_NAME]
            self.database_name=DATABASE_NAME

        except Exception as e:
            raise MyException(e,sys)