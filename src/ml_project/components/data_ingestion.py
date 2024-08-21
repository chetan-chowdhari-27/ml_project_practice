# MySql -->  Train Test Split --> Dataset 
import os
import sys
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str= os.path.joins('artifact','train.csv')
    test_data_path:str= os.path.joins('artifact','test.csv')
    raw_data_path:str= os.path.joins('artifact','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ## reading the code 
            logging.info('Reading from mysql database')
            
        except Exception as e:
            raise CustomException(e,sys)