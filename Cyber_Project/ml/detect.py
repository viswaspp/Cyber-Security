
import joblib, os
MODEL_PATH = "data/model.joblib"
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError("Model not trained. Run manage.py train_model")
    return joblib.load(MODEL_PATH)

def score_log(entry):
    clf = load_model()
    # create feature vector
    path_len = len(entry.get("path","/"))
    method_code = 0 if entry.get("method","GET")=="GET" else 1
    ua_len = len(entry.get("user_agent",""))
    ip_oct = int(entry.get("src_ip","0").split(".")[-1]) if "." in entry.get("src_ip","") else 0
    X = [[path_len, method_code, ua_len, ip_oct]]
    score = clf.predict(X)[0]  # -1 anomaly, 1 normal
    return score
