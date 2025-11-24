
import os
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

MODEL_PATH = "data/model.joblib"

def synthesize(n=1000):
    import random
    X = []
    for _ in range(n):
        # features: path length, method_code, ua_len, src_ip_last_octet
        path_len = random.randint(1,80)
        method_code = 0 if random.random()<0.8 else 1
        ua_len = random.randint(5,200)
        ip_oct = random.randint(1,250)
        X.append([path_len, method_code, ua_len, ip_oct])
    return X

def train_and_save_model():
    os.makedirs("data", exist_ok=True)
    X = synthesize(2000)
    clf = IsolationForest(contamination=0.02, random_state=42)
    clf.fit(X)
    joblib.dump(clf, MODEL_PATH)
    print("Saved model to", MODEL_PATH)

if __name__ == "__main__":
    train_and_save_model()
