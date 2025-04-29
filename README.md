# Loan Acceptance Prediction

## Introduction

Here is my project that leverages traditional machine learning models to predict whether a loan applicant should be approved or rejected. It emphasizes data quality and usability, with proper cleaning and preprocessing to filter out irrelevant or noisy features. The project also includes exploratory data analysis (EDA) to help understand patterns, relationships, and trends in the dataset. 

## Goals and Objectives
**Goal:**

Develop a predictive and interpretable machine learning model to assist banks in assessing the risk of potential loans and provide transparent, data-driven justifications to encourage investor confidence in lending decisions.

**Key objectives:**

- **Analyze:** To understand the structure and patterns within the dataset.

- **Develop Predictive Models:** That are robust and well-suited to predict the likelihood of loan approval for new applicants.

- **Evaluate Models**: Compare and evaluate the performance of different models.

- **Select the Best Model:** That is both practical for real-world deployment and highly interpretable.

## Dataset
![Dataset Context](dataset_image.png)
<!-- <div align="center">
    <img src="dataset_image.png" alt="Dataset Context" style="width:70%" />
</div> -->

The dataset used in this project is from [Kaggle's Loan Classification Dataset](https://www.kaggle.com/datasets/abhishek14398/loan-dataset/data) and included in the `/data` directory. It consists of customers' details for acceptance/rejection of loans. The dataset contains 2 files:
- [loan.csv](https://github.com/phuongvu0206/Loan-Acceptance-Prediction/blob/main/data/loan.csv): Contains data used to analyze and train machine learning models.
- [Data_Dictionary.xlsx](https://github.com/phuongvu0206/Loan-Acceptance-Prediction/blob/main/data/Data_Dictionary.xlsx): Contains a data dictionary containing the columns with the feature name and their respective description for loan acceptance and rejection status.

## Requirements

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```