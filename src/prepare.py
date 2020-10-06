# Write supporting functions here
def run():
    print("Prepare: Cleaning acquired data...")
    # Write code here
    print("Prepare: Completed!")
def prepare_zillow(df):
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
    df = pd.read_csv('./data/raw/zillow.csv')
    
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
    duplicate_columns_to_drop = ['calculatedbathnbr', 'finishedsquarefeet12', 'id']
    df = df.drop(columns=duplicate_columns_to_drop)
    # Filter columns for single family residences.
    df = df[df.propertylandusetypeid.isin([261, 262, 273, 279])]
    return df


def prepare_zillow_mvp(df):
    '''
    
    '''
    df = df[['bathroomcnt', 'bedroom', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt']]
    return df