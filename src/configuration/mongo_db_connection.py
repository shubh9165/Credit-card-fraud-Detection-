import os
import pymongo
from src.constants import DATABASE_NAME,MONGODB_URL_KEY
from src.exception.exception import MyException
from src.logger.logger import logging
import sys
from dotenv import load_dotenv

load_dotenv()

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
                logging.info("Mongodb data base connected sucessfully")

            self.clinet=MongoDbClint.clinet
            self.database=self.clinet[DATABASE_NAME]
            self.database_name=DATABASE_NAME
            logging.info("mongo_db_connection file work done")

        except Exception as e:
            raise MyException(e,sys)
