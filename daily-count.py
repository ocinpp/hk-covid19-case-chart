import requests
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib


def get_summary_df():
    # data: https://data.gov.hk/en-data/dataset/hk-dh-chpsebcddr-novel-infectious-agent/resource/5d278827-da7e-4461-9f63-222cf0c5da27
    #response = requests.get('http://www.chp.gov.hk/files/misc/enhanced_sur_pneumonia_wuhan_eng.csv', allow_redirects=True)
    response = requests.get(
        'http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv')
    file_object = io.StringIO(response.content.decode('utf-8'))
    df_confirmed_case = pd.read_csv(file_object)
    # df_confirmed_case['Name of hospital admitted'] = df_confirmed_case['Name of hospital admitted'].str.strip()
    df_confirmed_case['Hospitalised/Discharged/Deceased'] = df_confirmed_case['Hospitalised/Discharged/Deceased'].str.strip()
    df_confirmed_case['Case classification*'] = df_confirmed_case['Case classification*'].str.strip()
    df_confirmed_case['Confirmed/probable'] = df_confirmed_case['Confirmed/probable'].str.strip()
    df_confirmed_case['HK/Non-HK resident'] = df_confirmed_case['HK/Non-HK resident'].str.strip()
    df_confirmed_case = df_confirmed_case[df_confirmed_case['Confirmed/probable'] == 'Confirmed']
    return df_confirmed_case

def clean_data(df_reported_case):
    # case no. 1603 - 16/0了7/2020
    df_reported_case['Report date'] = df_reported_case['Report date'].str.replace('了', '')
    return df_reported_case


def get_date_df():
    #response = requests.get('http://www.chp.gov.hk/files/misc/latest_situation_of_reported_cases_wuhan_eng.csv')
    response = requests.get(
        'http://www.chp.gov.hk/files/misc/latest_situation_of_reported_cases_covid_19_eng.csv')
    file_object = io.StringIO(response.content.decode('utf-8'))
    df_reported_case = pd.read_csv(file_object)
    df_reported_case.drop_duplicates(inplace=True)

    # create dataframe with "all" dates since there are some dates without confirmed cases
    df_date_date = df_reported_case['As of date'].to_frame('Date')
    df_date_date['Date'] = pd.to_datetime(
        df_date_date['Date'], format='%d/%m/%Y')
    df_date_date = df_date_date.set_index('Date')
    return df_date_date


df_confirmed_case = get_summary_df()
df_confirmed_case = clean_data(df_confirmed_case)
df_date_date = get_date_df()

# Extract required columns
df_confirmed_case_group = df_confirmed_case.filter(
    ['Report date', 'Case classification*', 'Case no.'], axis=1)

# Rename columns
df_confirmed_case_group = df_confirmed_case_group.rename(
    columns={'Report date': 'Date', 'Case classification*': 'Case classification'})

# convert to date
df_confirmed_case_group['Date'] = pd.to_datetime(
    df_confirmed_case_group['Date'], format='%d/%m/%Y')

# set date as index
df_confirmed_case_group = df_confirmed_case_group.set_index('Date')

# group by date and classification
df_confirmed_case_group = df_confirmed_case_group.groupby(
    ['Date', 'Case classification']).count()['Case no.']

# unstack the dataframe
df_confirmed_case_group = df_confirmed_case_group.unstack()

# join "all" dates with case count of dates and fill N/A with 0
df_confirmed_case_group = df_date_date.join(df_confirmed_case_group).fillna(0)

# filter records
df_confirmed_case_group = df_confirmed_case_group[df_confirmed_case_group.index >= '2020-01-23']

# bar chart
ax = df_confirmed_case_group.plot.bar(figsize=(40, 10), rot=75,
                                      title='Number of Confirmed Cases of Coronavirus in Hong Kong',
                                      colormap='gist_rainbow',
                                      stacked=True)

# format date on x-axis
x_labels = df_confirmed_case_group.index.strftime('%d/%m/%Y')
ax.set_xticklabels(x_labels)
# plt.show()

date_str = df_date_date.index[-1].strftime("%Y%m%d")
filename = 'charts/' + 'daily-count-chart-' + date_str
# print(filename)
plt.savefig(filename)
