from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation  import ModelEvaluationPipeline
from TextSummarizer.pipeline.prediction  import PredictionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} started>>>")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} completed>>>")
except Exception as e:
    logger.error(f"<<<Pipeline stage: {STAGE_NAME} failed>>>")
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} started>>>")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} completed>>>")
except Exception as e:
    logger.error(f"<<<Pipeline stage: {STAGE_NAME} failed>>>")
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} started>>>")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} completed>>>")
except Exception as e:
    logger.error(f"<<<Pipeline stage: {STAGE_NAME} failed>>>")
    raise e

STAGE_NAME = 'Model Training'
try:
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} started>>>")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} completed>>>")
except Exception as e:
    logger.error(f"<<<Pipeline stage: {STAGE_NAME} failed>>>")
    raise e

STAGE_NAME = 'Model Evaluation'
try:
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} started>>>")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"<<<Pipeline stage: {STAGE_NAME} completed>>>")
except Exception as e:
    logger.error(f"<<<Pipeline stage: {STAGE_NAME} failed>>>")
    raise e
