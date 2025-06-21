try:
    # System & Environment
    import pyodbc
    from dotenv import load_dotenv
    print("Both pyodbc and dotenv were imported successfully.")

    # Core Libraries
    import numpy as np
    import pandas as pd
    import missingno as msno
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Preprocessing & Utilities
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score

    # Regression Models
    from sklearn.ensemble import (
        RandomForestRegressor,
        ExtraTreesRegressor,
        StackingRegressor,
        VotingRegressor
    )
    from sklearn.linear_model import Ridge, Lasso, ElasticNet
    from xgboost import XGBRegressor
    from lightgbm import LGBMRegressor

    # Evaluation
    from sklearn.metrics import mean_squared_error

except ImportError as e:
    print(f"Import failed: {e}")
