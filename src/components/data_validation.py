import os
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
import pandas as pd
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.constants import *
from src.utils.main_utils import read_yaml_file
import json

class DataValidation:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        self.data_ingestion_artifact=data_ingestion_artifact
        self.data_validation_config=data_validation_config
        self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)

    def validate_columns(self,df):
        try:
            logging.info("checking is there are same number of columns in dataframe or not  ")
            status=len(df.columns)==len(self._schema_config["columns"])
            logging.info(f"there are same number of columns {status}")
            return status
        except Exception as e:
            raise MyException(e,sys)
    
    def check_cato_numerical(self,df):
        try:
            logging.info("checking for numerical columns")
            dataframe_columns=df.columns
            missing_column=[]
            for columns in self._schema_config["numerical_columns"]:
                if columns not in dataframe_columns:
                    missing_column.append(columns)

            logging.info("checking of numerical columns done")
            return False if len(missing_column)>0 else True
        
        except Exception as e:
            raise MyException(e,sys)
        

    @staticmethod
    def read_file(file_path):
        try:
            df=pd.read_csv(file_path)
            return df
        except Exception as e:
            raise MyException(e,sys)
        

    def initiate_data_validation(self):
        try:
            logging.info("data validation word start")
            train_set,test_set=(self.read_file(self.data_ingestion_artifact.trained_file_path),
                                self.read_file(self.data_ingestion_artifact.test_file_path))
            
            logging.info("train and test data set load sucessfully")
            error_message=""
            logging.info("going into train data set")
            status=self.validate_columns(train_set)
            if not status:
                error_message+= f"Columns are missing in training dataframe. "
            else:
                logging.info("everything fine realatd to number of columns in train set")

            status=self.validate_columns(test_set)
            if not status:
                error_message+= f"Columns are missing in test dataframe."
            else:
                logging.info("everything fine realatd to number of columns in test set")

            logging.info("going into train data set")
            status=self.check_cato_numerical(train_set)

            if not status:
                error_message += f"Columns are missing in training dataframe. "
            else:
                logging.info(f"All categorical/int columns present in training dataframe: {status}")

            logging.info("going into test data set")

            status=self.check_cato_numerical(test_set)
            
            if not status:
                error_message += f"Columns are missing in test dataframe."
            else:
                logging.info(f"All categorical/int columns present in testing dataframe: {status}")

            validation_status=len(error_message)==0

            data_validationn_artifact=DataValidationArtifact(
                validation_status=validation_status,
                message=error_message,
                validation_report_file_path=self.data_validation_config.data_validation_report_file_name
            )

            report_dir = os.path.dirname(self.data_validation_config.data_validation_report_file_name)
            os.makedirs(report_dir, exist_ok=True)

            # Save validation status and message to a JSON file
            validation_report = {
                "validation_status": validation_status,
                "message": error_message.strip()
            }

            with open(self.data_validation_config.data_validation_report_file_name, "w") as report_file:
                json.dump(validation_report, report_file, indent=4)

            logging.info("Data validation artifact created and saved to JSON file.")
            logging.info(f"Data validation artifact: {data_validationn_artifact}")
            return data_validationn_artifact

        except Exception as e:
            raise MyException(e,sys)
        
