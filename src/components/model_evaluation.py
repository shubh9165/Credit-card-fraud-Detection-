import os
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
from src.constants import *
from src.entity.artifact_entity import ModelEvaluationArtifact, DataIngestionArtifact, ModelTrainerArtifact,DataTransformationArtifact
from src.entity.config_entity import ModelEvaluationConfig
from src.utils.main_utils import load_object, load_numpy_array_data
from sklearn.metrics import f1_score
from src.constants import TARGET_COLUMN
import pandas as pd
from typing import Optional
from src.entity.s3_estimator import Proj1Estimator
from dataclasses import dataclass


@dataclass
class EvaluateModelResponse:
    best_model_f1_score: float
    trained_model_f1_score: float
    is_model_accepted: bool
    difference: float


class ModelEvaluation:

    def __init__(self,
                 model_evaluation_config: ModelEvaluationConfig,
                 model_trainer_artifact: ModelTrainerArtifact,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_transformation_artifact:DataTransformationArtifact):

        self.model_evaluation_config = model_evaluation_config
        self.model_trainer_artifact = model_trainer_artifact
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_artifact=data_transformation_artifact


    def get_best_model(self) -> Optional[Proj1Estimator]:
        try:
            bucket_name = self.model_evaluation_config.bucket_name
            model_path = self.model_evaluation_config.s3_model_key_path

            proj1_estimator = Proj1Estimator(
                bucket_name=bucket_name,
                model_path=model_path
            )

            if proj1_estimator.is_model_present(model_path=model_path):
                return proj1_estimator

            return None

        except Exception as e:
            raise MyException(e, sys)


    def eval_model(self):
        try:


            test=pd.read_csv(self.data_ingestion_artifact.test_file_path)

            logging.info("Transformed numpy test datafreame loaded")

            processor=load_object(self.data_transformation_artifact.transformed_object_file_path)

            logging.info("processor loaded")

            test["Amount"]=processor.transform(test[["Amount"]])

            X,y=test.drop(columns=['Class'],axis=1),test['Class']

            trained_model = load_object(
                self.model_trainer_artifact.trained_model_file_path
            )
            logging.info("Trained model loaded")

            trained_model_f1_score = self.model_trainer_artifact.metrics_artifacts.f1_score
            best_model_f1_score = None

            best_model = self.get_best_model()

            if best_model is not None:
                logging.info("Computing F1 score for production model...")
                y_hat_best_model = best_model.predict(X)

                best_model_f1_score = f1_score(y, y_hat_best_model)

                logging.info(
                    f"F1 Score - Production Model: {best_model_f1_score}, "
                    f"New Model: {trained_model_f1_score}"
                )

            tmp_best_score = 0 if best_model_f1_score is None else best_model_f1_score

            result = EvaluateModelResponse(
                trained_model_f1_score=trained_model_f1_score,
                best_model_f1_score=best_model_f1_score,
                is_model_accepted=trained_model_f1_score > tmp_best_score,
                difference=trained_model_f1_score - tmp_best_score
            )

            logging.info(f"Evaluation Result: {result}")

            return result

        except Exception as e:
            raise MyException(e, sys)


    def initiate_model_evaluation(self):
        try:
            logging.info("Model evaluation started")

            evaluation_response = self.eval_model()

            model_eval_artifact = ModelEvaluationArtifact(
                is_model_accepted=evaluation_response.is_model_accepted,
                changed_accurecy=evaluation_response.difference,
                trained_model_path=self.model_trainer_artifact.trained_model_file_path,
                s3_model_path=self.model_evaluation_config.s3_model_key_path
            )

            logging.info("Model evaluation completed")

            return model_eval_artifact

        except Exception as e:
            raise MyException(e, sys)
