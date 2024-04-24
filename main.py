from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"Pipeline stage: {STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Pipeline stage: {STAGE_NAME} completed")
except Exception as e:
    logger.error(f"Pipeline stage: {STAGE_NAME} failed")
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"Pipeline stage: {STAGE_NAME} started")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"Pipeline stage: {STAGE_NAME} completed")
except Exception as e:
    logger.error(f"Pipeline stage: {STAGE_NAME} failed")
    raise e