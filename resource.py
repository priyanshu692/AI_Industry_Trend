import os
import kaggle
from huggingface_hub import HfApi

# Set up your Kaggle API key (Make sure to set it in the environment variable or pass the path to the Kaggle key)
os.environ['KAGGLE_CONFIG_DIR'] = "/path/to/kaggle.json"

def search_huggingface_datasets(query):
    api = HfApi()
    datasets = api.list_datasets(search=query)
    return [dataset.id for dataset in datasets]


def search_kaggle_datasets(query):
    kaggle.api.authenticate()
    datasets = kaggle.api.dataset_list(search=query)
    return [dataset.title for dataset in datasets]


if __name__ == "__main__":
    hf_datasets = search_huggingface_datasets("predictive maintenance")
    kaggle_datasets = search_kaggle_datasets("predictive maintenance")

    print("HuggingFace Datasets:", hf_datasets)
    print("Kaggle Datasets:", kaggle_datasets)
