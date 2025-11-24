
import os
from app.db import init_db
from ml.train import train_and_save_model

def init():
    init_db()
    print("DB initialized.")

def train_model():
    train_and_save_model()
    print("Model trained and saved.")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv)>1 else "help"
    if cmd=="init":
        init()
    elif cmd=="train_model":
        train_model()
    else:
        print("Usage: manage.py [init|train_model]")
