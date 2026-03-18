import os
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
from src.constants import *
from src.data_access.proj1_data import proj1
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self):

        try:
            self.data_ingestion_config=DataIngestionConfig()
        except Exception as e:
            raise MyException(e,sys)
        
    def get_data(self,collction_name):
        try:
            
            my_data=proj1()
            df=my_data.export_data(collction_name)
            logging.info("data frame loaded from mongodb and proj1 file work are done")

            df["Hour"] = df["Time"] / 3600
            df["Hour"] = df["Hour"] % 24

            df["time_diff"] = df["Time"].diff()
            df["time_diff"] = df["time_diff"].fillna(0)

            df.drop_duplicates(inplace=True)

            logging.info("Time series work are done")

            feature_store_dir=self.data_ingestion_config.feature_store_dir_name
            os.makedirs(os.path.dirname(feature_store_dir), exist_ok=True)
            df.to_csv(feature_store_dir,header=True,index=False)
            logging.info("raw data frame are stored sucessfully")
            return df
        except Exception as e:
            raise MyException(e,sys)
    
    
    def initiate_data_ingestion(self):

        try:
            logging.info("data ingestion initiation  process are start")
            data_frame=self.get_data(collction_name=DATA_INGESTION_COLLECTION_NAME)

            X=data_frame.drop(columns=['Class'])
            y=data_frame['Class']

            Train_data,Test_data=train_test_split(data_frame,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("data frame dividie into test and train")

            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_file_path),exist_ok=True)

            Train_data.to_csv(self.data_ingestion_config.training_file_path,header=True,index=False)
            Test_data.to_csv(self.data_ingestion_config.test_file_path,header=True,index=False)

            logging.info("train and test data saved")

            data_ingestion_artifact=DataIngestionArtifact(Train_data,Test_data)
            return data_ingestion_artifact

        except Exception as e:
            raise MyException(e,sys)
        
