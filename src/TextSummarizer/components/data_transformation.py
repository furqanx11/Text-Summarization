from TextSummarizer.logging import logger
from transformers import  AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.config.configuration import DataTransformationConfig
import os
import pandas as pd
from datasets import Dataset

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['text'], max_length= 1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length= 128, truncation=True)
        
        return{
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        df = pd.read_csv(self.config.data_path)

        dataset_bbc = Dataset.from_pandas(df)
    
        dataset_train_test = dataset_bbc.train_test_split(test_size=0.2)
        dataset_train = dataset_train_test['train']
        dataset_test = dataset_train_test['test']
        
        dataset_train_val = dataset_train.train_test_split(test_size=0.1)
        dataset_train = dataset_train_val['train']
        dataset_val = dataset_train_val['test']
        
        dataset_train = dataset_train.map(self.convert_examples_to_features, batched=True)
        dataset_val = dataset_val.map(self.convert_examples_to_features, batched=True)
        dataset_test = dataset_test.map(self.convert_examples_to_features, batched=True)

        dataset_train.save_to_disk(os.path.join(self.config.root_dir, 'train_dataset'))
        dataset_val.save_to_disk(os.path.join(self.config.root_dir, 'val_dataset'))
        dataset_test.save_to_disk(os.path.join(self.config.root_dir, 'test_dataset'))