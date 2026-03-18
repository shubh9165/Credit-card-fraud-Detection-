import os 
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()

    def start_data_ingestion(self):
        try:
            logging.info("Enter into data ingestion from training pipeline")
            data_ingestion=DataIngestion()
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("data Ingestion process completely done")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact,data_validation_config):
        try:
            logging.info("Enter into data validation from training pipeling")
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                           data_validation_config=data_validation_config)
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("data validation process are completely done")
            return data_validation_artifact
            

        except Exception as e:
            raise MyException(e,sys)
    def run_trainingpipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=self.data_validation_config)

        except Exception as e:
            raise MyException(e,sys)

if __name__=="__main__":
    obj=TrainingPipeline()
    obj.run_trainingpipeline()