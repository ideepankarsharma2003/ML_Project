import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    def __init__(self):
        # self.train_data_path: os.path.join('artifacts', 'train.csv')
        self.train_data_path= os.path.join('artifacts', 'train.csv')
        # self.test_data_path: os.path.join('artifacts', 'test.csv')
        self.test_data_path= os.path.join('artifacts', 'test.csv')
        # self.raw_data_path: os.path.join('artifacts', 'data.csv')
        self.raw_data_path= os.path.join('artifacts', 'data.csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion initiated...')
        print('Data ingestion initiated...')
        try:
            df= pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Raw data saved to artifacts folder')

            train, test= train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Split the data into train and test')

            train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info('Train data saved to artifacts folder')
            
            test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Test data saved to artifacts folder')
            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )




        except Exception as e:
            logging.error(e)
            raise CustomException(e, sys)
        

if __name__=="__main__":
    DataIngestion().initiate_data_ingestion()
