import warnings
warnings.filterwarnings

# Importing Pandas and NumPy
import pandas as pd, numpy as np

# Importing all datasets
churn_data = pd.read_csv("churn_data.csv")
churn_data.head()

customer_data = pd.read_csv("customer_data.csv")
customer_data.head()

internet_data = pd.read_csv("internet_data.csv")
internet_data.head()


# df_1 = pd.merge(churn_data, customer_data, how='inner', on='customerID')

# telecom = pd.merge(df_1, internet_data, how='inner', on='customerID')
