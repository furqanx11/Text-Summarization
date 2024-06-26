from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_tainer_config = config.get_model_trainer_config()
        model_tainer_config = ModelTrainer(config = model_tainer_config)
        model_tainer_config.train()
