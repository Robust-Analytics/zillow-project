# Write supporting functions here
import pandas as pd
from acquire import load_zillow_data

def run():
    print("Prepare: Cleaning acquired data...")
    # Write code here
    print("Prepare: Completed!")
    
    
def prepare_zillow():
    '''
    Signature: prepare_zillow(df) -> pandas.core.frame.DataFrame
    Docstring:
    Prepare the zillow dataset for data EDA
    Return DataFrame of zillow dataset
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    df is the Zillow dataset stored as `zillow.csv`
    Returns
    -------
    DataFrame of the zillow dataset
    Examples
    --------
    To copy the code hold ALT + SHIFT and drag your cursor from the first line to the last.
    df = pd.read_csv('zillow.csv')
    
    nulls = df.isnull().sum()
    non_nulls = df.notnull().sum()
    total_values = nulls + non_nulls
    pct_missing = (nulls/total_values).sort_values(ascending=False)
    pct_missing_chart = pct_missing.apply("{0:.2%}".format)
    
    print('Percentage of values missing per column')
    print('-' * 39)
    print(f"{pct_missing_chart}")
    '''
    # 1. Drop columns with missing values
    # Calculate the number of missing values and non-null values.
    df = load_zillow_data()
    nulls = df.isnull().sum()
    non_nulls = df.notnull().sum()
    # Get the total number values in each column.
    total_values = nulls + non_nulls
    # Create a variable to store the percentage of missing values in each column.
    # .3358 is a hard coded value from the original analysis.
    # To reproduce use the code in the docstring
    pct_missing = nulls/total_values
    columns_to_drop = pct_missing[pct_missing > .3358].index.to_list()
    # drop columns missing more than 33.58% of data.
    df = df.drop(columns=columns_to_drop)
    # drop duplicate columns and index column
    duplicate_columns_to_drop = ['calculatedbathnbr', 'finishedsquarefeet12', 'id', 'id.1', 'logerror']
    df = df.drop(columns=duplicate_columns_to_drop)
    # Filter columns for single family residences.
    df = df[df.propertylandusetypeid.isin([261, 262, 273])]
    #  df = df.dropna()
    df = df[(df['bathroomcnt'] > 0) & (df['bathroomcnt'] > 0)]
    df.drop(columns=['transactiondate', 'latitude', 'longitude', 'rawcensustractandblock',
                     'regionidcity', 'regionidcounty', 'regionidzip', 'censustractandblock',
                      'assessmentyear'], inplace = True)                     
    return df


def prepare_zillow_mvp():
    '''
    
    '''
    # Load in the zillow data
    df = load_zillow_data()
    
    # Drop properties that are not considered single family properties
    df = df[df.propertylandusetypeid.isin([261, 262, 273])]
    
    # Filter columns for MVP
    df = df[['bathroomcnt', 'bedroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt']]
    
    # Drop rows with missing values
    df = df.dropna()
    
    # Drop properties that don't have a room or a restroom
    df = df[(df['bathroomcnt'] > 0) & (df['bathroomcnt'] > 0)]
    df['more_than_two_bath'] = (df.bathroomcnt > 2).astype('int')
 
    return df