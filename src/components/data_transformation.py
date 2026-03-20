import os 
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
from src.constants import *
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from src.utils.main_utils import save_numpy_array_data,save_object
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import numpy as np


class DataTransformation:
    def __init__(self,data_ingestion_artifact,data_validation_artifact,data_transformation_config):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config
        except Exception as e:
            raise MyException(e,sys)
        

    @staticmethod
    def read_file(file_path)->pd.DataFrame:
        try:
           return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e,sys)
        
    def initiate_data_transformation(self):
        try:
            logging.info("Data Transformation process start")

            if not self.data_validation_artifact.validation_status:
                raise Exception(self.data_validation_artifact.message)

            train_set=self.read_file(self.data_ingestion_artifact.trained_file_path)
            test_set=self.read_file(self.data_ingestion_artifact.test_file_path)

            logging.info("train and test data load sucessfully")

            input_train_df=train_set.drop(columns=['Class'],axis=1)
            traget_train_df=train_set['Class']

            input_test_df=test_set.drop(columns=['Class'],axis=1)
            target_test_df=test_set['Class']

            logging.info("train and test data are divide into input and target df")

            processor=StandardScaler()
            logging.info("standard scaling work are start")

            input_train_df['Amount']=processor.fit_transform(input_train_df[['Amount']])

            input_test_df['Amount']=processor.transform(input_test_df[['Amount']])

            logging.info("Standard scaler work done on input train and test df")
            
            logging.info("The work of handling imblance data set are start")
            smt=SMOTE(random_state=42)

            input_train_df,traget_train_df=smt.fit_resample(input_train_df,traget_train_df)


            logging.info("all smote work are done")

            train_arr = np.c_[input_train_df.to_numpy(), np.array(traget_train_df)]
            test_arr = np.c_[input_test_df.to_numpy(), np.array(target_test_df)]

            logging.info("all data frame are converted into array")

            save_object(self.data_transformation_config.transformed_obj_dir,processor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,test_arr)

            data_transformation_artifact=DataTransformationArtifact(
                    transformed_object_file_path=self.data_transformation_config.transformed_obj_dir,
                    transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                    transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

            return data_transformation_artifact

        except Exception as e:
            raise MyException(e,sys)