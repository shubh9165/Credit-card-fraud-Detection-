import os
from src.constants import *
from dataclasses import dataclass

@dataclass
class TrainingPipelineConfig:
    pipeline_name:str=PIPELINE_NAME
    artifact_dir:str=os.path.join(os.getcwd(),ARTIFACT_DIR)


Training_Pipeline_Config=TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir_name:str=os.path.join(Training_Pipeline_Config.artifact_dir,DATA_INGESTION_DIR_NAME)
    feature_store_dir_name:str=os.path.join(Training_Pipeline_Config.artifact_dir,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME)
    training_file_path:str=os.path.join(data_ingestion_dir_name,DATA_INGESTION_TRAIN_DATA_DIR,TRAIN_FILE_NAME)
    test_file_path:str=os.path.join(data_ingestion_dir_name,DATA_INGESTION_TEST_DATA_DIR,TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME

@dataclass
class DataValidationConfig:
    data_validation_dir_name:str=os.path.join(Training_Pipeline_Config.artifact_dir,DATA_VALIDATION_DIR_NAME)
    data_validation_report_file_name:str=os.path.join(data_validation_dir_name,DATA_VALIDATION_REPORT_FILE_NAME)

    
@dataclass
class DataTransformationConfig:
    data_transformation_dir_name:str=os.path.join(Training_Pipeline_Config.artifact_dir,DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path:str=os.path.join(data_transformation_dir_name,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                       TRAIN_FILE_NAME.replace('csv','npy'))
    transformed_test_file_path:str=os.path.join(data_transformation_dir_name,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                            TEST_FILE_NAME.replace('csv','npy'))
    transformed_obj_dir:str=os.path.join(data_transformation_dir_name,DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                     PREPROCSSING_OBJECT_FILE_NAME)