import os
import sys
from src.exception.exception import MyException
from src.logger.logger import logging
from src.utils.main_utils import load_numpy_array_data,load_object,save_object
from src.entity.config_entity import ModelTrainerConfig,DataTransformationConfig
from src.constants import *
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact,ModelTrainerArtifact,ClassificationMetricsArtifacts
from xgboost import XGBClassifier
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score
from src.entity.estimator import MyModel

class ModelTrainer:
    def __init__(self,data_transforamtion_artifact,model_trainer_config):
        self.data_transformation_artifacts=data_transforamtion_artifact
        self.model_trainer_config=model_trainer_config

    def get_load(self,train,test):
        try:
            X_train,y_train,X_test,y_test=train[:, :-1], train[:, -1], test[:, :-1], test[:, -1]
            logging.info("train and test split sucessfully")

            xgb_model = XGBClassifier(
                n_estimators=MODEL_TRAINER_N_ESTIMATORS,
                learning_rate=MODEL_TRAINER_LEARNING_RATE,
                max_depth=MODEL_TRAINER_MAX_DEPTH,
                min_child_weight=MODEL_TRAINER_MIN_CHILD_WEIGHT,
                gamma=MODEL_TRAINER_GAMMA,
                subsample=MODEL_TRAINER_SUBSAMPLE,
                eval_metric=MODEL_TRAINER_EVAL_METRIC,
                random_state=42,
            )

            logging.info("fiting the model")

            xgb_model.fit(X_train,y_train)
            logging.info("model fiting done")

            y_pred=xgb_model.predict(X_test)

            logging.info("prediction done")

            accuracy=accuracy_score(y_test, y_pred)
            precision=precision_score(y_test, y_pred)
            f1=f1_score(y_test, y_pred)
            recall=recall_score(y_test, y_pred)

            logging.info("Model evaluation done")

            matrics_artifact=ClassificationMetricsArtifacts(
                accuracy_score=accuracy,
                precision_score=precision,
                f1_score=f1,
                recall_score=recall
            )

            return xgb_model,matrics_artifact

        except Exception as e:
            raise MyException(e,sys)
        

    def initiate_model_trainer(self):
        try:

            logging.info("model Training process start")

            train=load_numpy_array_data(self.data_transformation_artifacts.transformed_train_file_path)
    
            test=load_numpy_array_data(self.data_transformation_artifacts.transformed_test_file_path)

            logging.info("train and test arr are loaded")

            model,matrics=self.get_load(train,test)

            logging.info("model and metrics are loaded")

            procesor=load_object(self.data_transformation_artifacts.transformed_object_file_path)
            logging.info("processor object are loaded")

            if accuracy_score(train[:, -1], model.predict(train[:, :-1])) < EXEPECTED_ACCURACY:
                logging.info("No model found with score above the base score")
                raise Exception("No model found with score above the base score")

            my_model=MyModel(procesor,model)

            logging.info("my model are loaded sucessfully")

            save_object(self.model_trainer_config.trained_model_file_path,my_model)

            logging.info("my model are saved")

            model_trainer_artifact=ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                metrics_artifacts=matrics
            )

            return model_trainer_artifact

        except Exception as e:
            raise MyException(e,sys)

