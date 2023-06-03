import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('model.pkl', 'rb') as file:
	model = pickle.load(file)


# Define the Streamlit app
def main():
	st.title("Daily Active Minutes Prediction")

	# Get user input values
	day_of_week = st.slider("Select the day of the week", 0, 6)
	promotion_value = st.slider("Enter the promotion value (0-100)", 0, 100)
	happiness_index = st.slider("Enter the happiness index (1-5)", 1, 5)

	# Create a numpy array with the user input values
	input_data = np.array([[day_of_week, promotion_value, happiness_index]])

	# Make the prediction
	predicted_minutes = model.predict(input_data)

	# Display the predicted daily active minutes
	st.write("Predicted Daily Active Minutes: {:.2f}".format(predicted_minutes[0]))

# Run the Streamlit app
if __name__ == '__main__':
	main()
