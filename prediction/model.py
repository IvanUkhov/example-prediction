import pandas as pd


class Model:

    def fit(self, data):
        self.alpha = 0.42
        self.beta = -0.24

    def predict(self, data):
        score = self.alpha * data['deposit'] + self.beta * data['withdrawal']
        return pd.DataFrame(dict(label=score > 0))
