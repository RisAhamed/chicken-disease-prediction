from src.CNN_Classifier.constants import  CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.CNN_Classifier.utils.common import read_yaml,create_directories
from src.CNN_Classifier import logger
from pathlib import Path
from src.CNN_Classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path =Path(CONFIG_FILE_PATH),
                  params_file_path = Path(PARAMS_FILE_PATH)):
        self.config_file_path = config_file_path
        self.params_file_path = params_file_path
        logger.info(f"Reading configuration file from: {self.config_file_path}")
        self.config = read_yaml(self.config_file_path)
        logger.info(f"Reading parameters file from: {self.params_file_path}")
        self.params = read_yaml(self.params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config