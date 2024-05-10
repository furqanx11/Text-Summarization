import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
import os
from TextSummarizer.config.configuration import DataIngestionConfig
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")
        
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)

        stop_words = set(stopwords.words('english'))
        words = text.split()
        words = [word for word in words if word not in stop_words]
        text = ' '.join(words)

        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
        text = ' '.join(words)

        return text
    
    def merge(self):

        categories = ['sport', 'business', 'entertainment', 'politics', 'tech']  
        articles_dir = f'{self.config.load_data_dir}/News Articles'
        summaries_dir = f'{self.config.load_data_dir}/Summaries'

        data = []

        for category in categories:
            article_files = os.listdir(os.path.join(articles_dir, category))
            for file in article_files:
                with open(os.path.join(articles_dir, category, file), 'r', encoding='latin-1') as f_article, \
                    open(os.path.join(summaries_dir, category, file), 'r', encoding='latin-1') as f_summary:
                    data.append({'text': f_article.read(), 'summary': f_summary.read()})

        df = pd.DataFrame(data)
        df['text'] = df['text'].apply(self.clean_text)
        df['summary'] = df['summary'].apply(self.clean_text)
        df.to_csv(os.path.join(self.config.root_dir, 'dataset.csv'), index=False)

