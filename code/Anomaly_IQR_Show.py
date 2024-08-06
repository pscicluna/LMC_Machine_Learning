import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Limited_Sample10000.csv', sep=',')

# Feature columns
features = ['magU', 'magB', 'magV', 'magI', 'magJ', 'magH', 'magK', 'mag3_6', 'mag4_5', 'mag5_8', 'mag8_0', 'mag24']

# Create a copy of the dataframe to work on
df_copy = df.copy()

# Calculate the IQR for each feature
Q1 = df_copy[features].quantile(0.25)
Q3 = df_copy[features].quantile(0.75)
IQR = Q3 - Q1

# Determine the upper and lower bounds for anomalies
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Function to identify anomalies
def find_anomalies(df, feature):
    return df[(df[feature] < lower_bound[feature]) | (df[feature] > upper_bound[feature])]

# Plotting anomalies for each feature
for feature in features:
    anomalies = find_anomalies(df_copy, feature)
    plt.figure(figsize=(12, 6))
    sns.histplot(df_copy[feature], kde=True, color='blue', label='Normal Data')
    sns.histplot(anomalies[feature], kde=True, color='red', label='Anomalies')
    plt.axvline(lower_bound[feature], color='green', linestyle='dashed', linewidth=1)
    plt.axvline(upper_bound[feature], color='green', linestyle='dashed', linewidth=1)
    plt.title(f'Anomalies in {feature}')
    plt.legend()
    plt.show()

# Mark anomalies in the dataset
for feature in features:
    df_copy[f'{feature}_anomaly'] = ((df_copy[feature] < lower_bound[feature]) | (df_copy[feature] > upper_bound[feature])).astype(int)

# Save the results with anomalies marked
df_copy.to_csv('Limited_Sample10000_with_anomalies.csv', sep='\t', index=False)

print("Anomalies have been identified and saved to 'Limited_Sample10000_with_anomalies.csv'.")

