# Zillow Project

## __Robust Analytics™__

__Anthony Straine__<br>
Junior Data Scientist

__Christopher Ortiz__<br>
Junior Data Scientist

## Description

Predict the market value of single unit properties using properties that were sold in May and June of 2017.

## Summary

Working together we discovered for our MVP that the features that appear to drive home value as measure by taxvaluedollarcnt are bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet. We discovered this by going through an iterative, manual process of feature selection using a Pearson's R correlation test to select the top two features of bathroomcnt and calculatedfinishedsquarefeet and using industry knowledge to also include calculatedfinishedsquarefeet and homes having more than 2 bathrooms.

After testing a few models, a polynomial model performed the best. Features used in our model:
- bathroomcnt
- bedroomcnt
- calculatedfinishedsquarefeet
- taxvaluedollarcnt

These features explain 47% of the variance in the tax value dollar amount. For our next iteration we will look at additional features while controlling for outliers.

## Data Dictionary

| Feature | Definition | Data Type | 
| --- | --- | --- |
| id | row index number, range: 0 - 2985216 | int64 |
| parcelid | Unique numeric id assigned to each property: 10711725 - 169601949  | int64 |
| bathroomcnt | Number of bathrooms a property has: 0 - 32 | float64 | 
| bedroomcnt | Number of bedrooms a property has: 0 - 25  | float64 |
| calculatedfinishedsquarefeet | Number of square feet of the property: 1 - 952576 | float64 |
| fips | [(FIPS)](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) Five digit number of which the first two are the FIPS code of the state to which the county belongs. Leading 0 is removed from the data: 6037=Los Angeles County, 6059=Orange County, 6111=Ventura County | float64 |
| fullbathcnt | Number of full bathrooms a property has: 1 - 32 | float64 |
| latitude| Latitude of the middle of the parcel multiplied by 10e6 | float64 |
| longitude | Longitude of the middle of the parcel multiplied by 10e6 | float64 |
| lotsizesquarefeet |The land the property occupies in squared feet : 100 - 371000512 | float64 |
| propertylandusetypeid | Unique numeric id that identifies what the land is used for: the 261=Single Family Residential, 262=Rural Residence, 273=Bungalow | float64 |
| regionidcity |  City in which the property is located (if any) | float64 |
| regionidcounty | County in which the property is located | float64 |
| regionidzip | Zip code in which the property is located | float64 |
| roomcnt | Total number of rooms in the principal residence | float64 |
| yearbuilt | Year the property was built | float64 |
| structuretaxvaluedollarcnt | The assessed value of the built structure on the parcel | float64 |
| assessmentyear | The year of the property tax assessment  | float64 |
| landtaxvaluedollarcnt | The assessed value of the land area of the parcel | float64 |
| censustractandblock | Census tract and block ID combined - also contains blockgroup assignment by extension | float64 |
 
| Target | Definition | Data Type |
| --- | --- | --- |
| taxamount | The total property tax assessed for that assessment year | float64 |
| taxvaluedollarcnt |The total tax assessed value of the parcel | float64 |


## Project Organization
```
├── README.md           <- The top-level README for developers using this project.
│
│
├── mvp.ipynb           <- The main notebook for the project
│
│
├── acquire.py          <- The script to download or generate data
│
├── prepare.py          <- The script for preparing the raw data
│
├── wrangle.py          <- The script for preparing the raw data for exploration
│
├── model.py            <- The script for preprocessing, modeling, and interpreting
```

## Requirements
---
- numpy >= 1.1.2
- pandas >= 1.18.1
- scipy >=1.4.1
- sklearn >= 0.23.2
- matplotlib >= 3.3.1
- seaborn >= 0.11.0

## Setup
1. Download a zip file of the repository [here](https://github.com/Robust-Analytics/zillow-project/archive/main.zip)

2. Clone this repository using:
```
$ git clone git@github.com:Robust-Analytics/zillow-project.git
```

To open the file in a jupyter notebook use following code:
``` python
import pandas as pd
df = pd.read_csv('zillow.csv')
```

## Acknowledgements
- Codeup Data Science Team
- Darden Cohort
- Generated with [ryans_codeup_data_science_mvp](https://github.com/RyanMcCall/-ryans_codeup_data_science_mvp)

## Contact
How to reach Anthony
- [@DataStraine](https://twitter.com/datastraine)
- - 📫 anthony.straine@gmail.com

How to reach Chris
- [@Promeos42](https://twitter.com/Promeos42)
- 📫 christopher.logan.ortiz@gmail.com