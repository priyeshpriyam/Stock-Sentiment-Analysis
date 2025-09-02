# verify_install.py
try:
    import pandas
    import numpy
    import sklearn
    import matplotlib
    import seaborn
    import yfinance
    import nltk
    import transformers
    import torch
    import tensorflow
    import flask
    import streamlit
    import xgboost
    import requests
    import jupyterlab

    print("✅ All libraries installed successfully!")
    print("\n--- Library Versions ---")
    print(f"Pandas: {pandas.__version__}")
    print(f"NumPy: {numpy.__version__}")
    print(f"Scikit-learn: {sklearn.__version__}")
    print(f"Transformers: {transformers.__version__}")
    print(f"PyTorch: {torch.__version__}")
    print(f"TensorFlow: {tensorflow.__version__}")
    print(f"XGBoost: {xgboost.__version__}")
    print("----------------------")

except ImportError as e:
    print(f"❌ Error: A library is missing!")
    print(f"Details: {e}")