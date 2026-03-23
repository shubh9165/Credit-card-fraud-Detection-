from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message:str
    validation_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ClassificationMetricsArtifacts:
    accuracy_score:float
    precision_score:float
    recall_score:float
    f1_score:float
    

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str
    metrics_artifacts:ClassificationMetricsArtifacts

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accurecy:float
    trained_model_path:str
    s3_model_path:str

@dataclass
class ModelPusherArtifact:
        bucket_name:str
        s3_model_path:str
