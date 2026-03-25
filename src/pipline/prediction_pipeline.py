import sys
from src.entity.config_entity import CreditCardConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception.exception import MyException
from src.logger.logger import logging
from pandas import DataFrame


class CreditCardData:
    def __init__(self,
                Time,
                V1,
                V2,
                V3,
                V4,
                V5,
                V6,
                V7,
                V8,
                V9,
                V10,
                V11,
                V12,
                V13,
                V14,
                V15,
                V16,
                V17,
                V18,
                V19,
                V20,
                V21,
                V22,
                V23,
                V24,
                V25,
                V26,
                V27,
                V28,
                Amount,
                Hour,
                time_diff
                ):
        try:
            self.Time = Time
            self.V1 = V1
            self.V2 = V2
            self.V3 = V3
            self.V4 = V4
            self.V5 = V5
            self.V6 = V6
            self.V7 = V7
            self.V8 = V8
            self.V9 = V9
            self.V10 = V10
            self.V11 = V11
            self.V12 = V12
            self.V13 = V13
            self.V14 = V14
            self.V15 = V15
            self.V16 = V16
            self.V17 = V17
            self.V18 = V18
            self.V19 = V19
            self.V20 = V20
            self.V21 = V21
            self.V22 = V22
            self.V23 = V23
            self.V24 = V24
            self.V25 = V25
            self.V26 = V26
            self.V27 = V27
            self.V28 = V28
            self.Amount =Amount
            self.Hour = Hour
            self.time_diff = time_diff

        except Exception as e:
            raise MyException(e, sys) from e

    def get_CreditCard_data_frame(self) -> DataFrame:
        try:
            credit_card_input_dict = self.get_CreditCard_data_as_dict()
            return DataFrame(credit_card_input_dict)
        
        except Exception as e:
            raise MyException(e, sys) from e


    def get_CreditCard_data_as_dict(self):
        logging.info("Entered get_CreditCard_data_as_dict method")

        try:
            input_data = {
                "Time": [self.Time],
                "V1": [self.V1],
                "V2": [self.V2],
                "V3": [self.V3],
                "V4": [self.V4],
                "V5": [self.V5],
                "V6": [self.V6],
                "V7": [self.V7],
                "V8": [self.V8],
                "V9": [self.V9],
                "V10": [self.V10],
                "V11": [self.V11],
                "V12": [self.V12],
                "V13": [self.V13],
                "V14": [self.V14],
                "V15": [self.V15],
                "V16": [self.V16],
                "V17": [self.V17],
                "V18": [self.V18],
                "V19": [self.V19],
                "V20": [self.V20],
                "V21": [self.V21],
                "V22": [self.V22],
                "V23": [self.V23],
                "V24": [self.V24],
                "V25": [self.V25],
                "V26": [self.V26],
                "V27": [self.V27],
                "Amount": [self.Amount],
                "Class": [self.Class],
                "Hour": [self.Hour],
                "time_diff": [self.time_diff]
            }

            logging.info("Created vehicle data dict")
            return input_data

        except Exception as e:
            raise MyException(e, sys) from e


class CreditCardDataClassifier:
    def __init__(self, prediction_pipeline_config: CreditCardConfig = CreditCardConfig()) -> None:
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe) -> str:
        try:
            logging.info("Entered predict method")

            model = Proj1Estimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )

            result = model.predict(dataframe)
            return result
        
        except Exception as e:
            raise MyException(e, sys)