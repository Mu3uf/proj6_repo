import os
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

def train():
    np.random.seed(42)
    normal_data = np.random.normal(loc=[1, 10, 2], scale=[0.5, 3, 1], size=(1000, 3))
    anomalous_data = np.random.uniform(low=[10, 100, 20], high=[50, 500, 100], size=(50, 3))
    X = np.vstack([normal_data, anomalous_data])
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    joblib.dump(model, os.path.join(os.path.dirname(__file__), "isolation_forest.joblib"))

if __name__ == "__main__":
    train()