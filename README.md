# Credit Card Fraud Detection Project

This Python project focuses on credit card fraud detection using machine learning and data preprocessing techniques. It aims to identify potentially fraudulent credit card transactions to help financial institutions and credit card companies prevent fraudulent activities.

## Data Sources
The project utilizes two main datasets:

1. [`application_record.csv`](https://huggingface.co/datasets/liberatoratif/Credit-card-fraud-detection/tree/main): Contains information about customers, including demographics, education, housing, and employment details.

2. [`credit_record.csv`](https://huggingface.co/datasets/liberatoratif/Credit-card-fraud-detection/tree/main): Contains records of credit card usage, including monthly balances and statuses.

## Data Preprocessing
To prepare the data for machine learning models, the following preprocessing steps were performed:

- Merging the two datasets based on the 'ID' column.
- Handling missing values by dropping rows with missing data.
- Encoding categorical variables and one-hot encoding categorical features.
- Scaling numerical features using the StandardScaler.

## Machine Learning Models
The project employs an ensemble model for credit card fraud prediction, combining various classifiers such as Gradient Boosting, XGBoost, LightGBM, AdaBoost, and CatBoost. The models are trained and evaluated using performance metrics, including ROC-AUC and classification reports.

## Usage
To use the credit card fraud detection system, you can input information about a potential credit card applicant, including demographics, income, employment details, and more. The system will then predict the likelihood of different credit card statuses for that applicant, ranging from overdue to paid off or no loan.

For more details, refer to the provided Python code.

Please note that this project is for educational purposes and should not be used in a production environment without further refinement and testing.

