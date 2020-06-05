import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import numpy as np

# Read in data
# source: https://data.seattle.gov/Permitting/Special-Events-Permits/dm95-f8w5
data_folder = '../data/'
data_file = 'Special_Events_Permits_2016.csv'
df = pd.read_csv(data_folder + data_file)

# Set aside 25% as test data
df_train, df_test = train_test_split(df, random_state=4321)

# Take a look
df_train.head()

# SIMPLE MODEL

# Binary outcome
y_train = np.where(df_train.permit_status == 'Complete', 1, 0)
y_test = np.where(df_test.permit_status == 'Complete', 1, 0)

# Single feature
X_train_1 = df_train[['attendance']].fillna(value=0)
X_test_1 = df_test[['attendance']].fillna(value=0)

# Fit model
model_1 = LogisticRegression(random_state=5678)
model_1.fit(X_train_1, y_train)
y_pred_train_1 = model_1.predict(X_train_1)
p_pred_train_1 = model_1.predict_proba(X_train_1)[:, 1]

# Evaluate model
# baseline: always predict the average
p_baseline_test = [y_train.mean()]*len(y_test)
auc_baseline = roc_auc_score(y_test, p_baseline_test)
print(auc_baseline)  # 0.5
y_pred_test_1 = model_1.predict(X_test_1)
p_pred_test_1 = model_1.predict_proba(X_test_1)[:, 1]
auc_test_1 = roc_auc_score(y_test, p_pred_test_1)
print(auc_test_1)  # 0.576553672316