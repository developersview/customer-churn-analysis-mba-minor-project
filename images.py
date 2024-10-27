#import libraries
import numpy as np #for various numerical operations
import pandas as pd #for processing of data
import plotly.express as px #for data visualization
import matplotlib.pyplot as plt #for data visualization

#set options
pd.set_option('display.max_columns', None)

#Read the dataset
customer_data = pd.read_csv("telco.csv")

#description and overview of the dataset
def data_overview(df, message):
    print(f'{message}:\n')
    print('Number of Rows: ', df.shape[0])
    print("\nNumber of Columns: ", df.shape[1])
    print('\nColumn Names in the dataset:')
    print(df.columns.tolist())

data_overview(customer_data, 'Overview of the dataset')