import os
import pandas as pd
import pickle

from prediction.model import Model


class Task:

    def run(self, action, config):
        getattr(self, '_process_' + action)(**config)

    def _process_training(self, data_path, output_path):
        data = pd.read_csv(data_path, index_col=0)
        model = Model()
        model.fit(data)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        model_path = os.path.join(output_path, 'model.pickle')
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)

    def _process_application(self, data_path, model_path, output_path):
        data = pd.read_csv(data_path, index_col=0)
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        predictions = model.predict(data)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        predictions_path = os.path.join(output_path, 'predictions.csv')
        predictions.to_csv(predictions_path, header=True)
