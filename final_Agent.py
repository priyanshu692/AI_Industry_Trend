def create_final_report(use_cases, hf_datasets, kaggle_datasets):
    report = f"""
    # AI Use Cases Proposal

    ## Proposed Use Cases:
    {use_cases}

    ## Relevant Resources:
    ### HuggingFace Datasets:
    {', '.join(hf_datasets)}

    ### Kaggle Datasets:
    {', '.join(kaggle_datasets)}
    """
    return report


if __name__ == "__main__":
    use_cases = """
    1. **Predictive Maintenance for Automotive Parts**: By leveraging machine learning models to predict when critical automotive components are likely to fail, companies can reduce downtime and maintenance costs.
    2. **AI-driven Supply Chain Optimization**: Using AI to forecast demand, optimize inventory levels, and automate order fulfillment in real-time, reducing costs and increasing efficiency.
    3. **Personalized Customer Experience in the Automotive Industry**: Deploying AI-powered chatbots or virtual assistants to help customers with car recommendations, maintenance scheduling, and answering FAQs, improving customer service.
    """

    hf_datasets = ["automotive-maintenance-dataset", "vehicle-anomaly-detection-model"]
    kaggle_datasets = ["predictive-maintenance-dataset", "automotive-supply-chain-forecast"]

    final_report = create_final_report(use_cases, hf_datasets, kaggle_datasets)
    print(final_report)
