import os
import pandas as pd
import pickle

from prediction.model import Model


class Task:

    def run(self, action, config):
        # Call the right handler for the action
        getattr(self, '_process_' + action)(**config)

    def _process_training(self, data_path, output_path):
        # Read the training data from a CSV file
        data = pd.read_csv(data_path, index_col=0)
        # Train the model
        model = Model()
        model.fit(data)
        # Ensure that the output directory exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # Save the trained model in a Pickle file
        model_path = os.path.join(output_path, 'model.pickle')
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)

    def _process_application(self, data_path, model_path, output_path):
        # Read the application data from a CSV file
        data = pd.read_csv(data_path, index_col=0)
        # Load the trained model from a Pickle file
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        # Make predictions
        predictions = model.predict(data)
        # Ensure that the output directory exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # Save the predictions in a CSV file
        predictions_path = os.path.join(output_path, 'predictions.csv')
        predictions.to_csv(predictions_path, header=True)
