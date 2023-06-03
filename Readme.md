# Streamlit App for Daily Active Minutes Prediction

This repository contains code for a Streamlit app that predicts daily active minutes based on user input values. It includes the following components:

## Data Analysis and Model Building

The `assignment_ml_neumile.ipynb` notebook contains code for data analysis, model building, and evaluation. It performs the following tasks:

- Loads and explores the 'user_engagement.csv' dataset.
- Conducts exploratory data analysis (EDA) and visualizes the data.
- Prepares the data by handling missing values and splitting it into training and testing sets.
- Builds several machine learning models, including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
- Evaluates the models using mean squared error (MSE), root mean squared error (RMSE), mean absolute error (MAE), and R-squared (R2) metrics.
- Identifies Linear Regression as the best fit model based on the evaluation metrics.
- Uses GridSearchCV to tune hyperparameters for the Linear Regression model.
- Trains the Linear Regression model with the best hyperparameters and saves it using joblib.

## Streamlit App

The `app.py` file contains the code for the Streamlit app. It provides a web interface for users to input values and get predictions for daily active minutes. The app includes the following functionalities:

- Displays a title and input sliders for the day of the week, promotion value, and happiness index.
- Uses the trained Linear Regression model to make predictions based on the user input values.
- Shows the predicted daily active minutes on the app interface.

## Instructions

To run the Streamlit app and perform data analysis, follow these steps:

1. Install the required packages by running `pip install -r requirements.txt`.
2. Ensure that the 'user_engagement.csv' dataset is placed in the appropriate directory.
3. Run the Streamlit app by executing `streamlit run app.py` in a terminal or command prompt.
4. Access the app through the provided URL (usually `http://localhost:8501`) in a web browser.
5. Interact with the app by adjusting the sliders and observing the predicted daily active minutes.
6. Explore the `assignment_ml_neumile.ipynb` notebook for detailed data analysis and model building steps.

Feel free to modify the code, dataset, and add additional functionalities to suit your specific requirements.

