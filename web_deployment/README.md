
# Instructions for Deploying Model to Web Application

## Overview

This guide explains how to deploy and run a machine learning model using Streamlit. The deployment package contains a pre-trained model that predicts loan classifications and includes necessary preprocessing tools.

## Project Structure

Inside the `web_deployment` folder, you will find:

- `loan_classifier_model.pkl` – The pre-trained machine learning model used for prediction.
- `scaler.pkl` – A file containing the standard scaler used to normalize input data.
- `web_deploy.py` – A Streamlit application providing a user interface for model interaction.

## Deployment Instructions

Follow these steps to deploy the application:

### 1. Open Terminal and Navigate to the Deployment Folder

```bash
cd "path/to/web_deployment"
```

Replace `"path/to/web_deployment"` with the actual path to your `web_deployment` directory.

### 2. Run Streamlit

Start the application by running:

```bash
streamlit run web_deploy.py
```

If successful, your terminal will display a local URL where you can view the app in your browser.

### 3. Fix File Path Errors (If Any)

If you encounter errors related to loading `.pkl` files, update the file paths of `loan_classifier_model.pkl` and `scaler.pkl` in function `load_model_and_scaler()` to their absolute paths if needed.

**Example:**

Replace:
```python
open("loan_classifier_model.pkl", "rb")
```

With:
```python
open("C:/Users/your_path/web_deployment/loan_classifier_model.pkl", "rb")
```

### 4. Restart the Application

After correcting the file paths, re-run the app:

```bash
streamlit run web_deploy.py
```

Ensure all `.pkl` files are located in the correct folder and paths are set properly.

## Application Interface

Once the application is running, the user interface will be accessible via your browser. You can then input new loan application data and view the model's prediction directly from the interface.
