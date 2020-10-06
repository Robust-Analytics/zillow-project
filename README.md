# Zillow Project

### Data Science Team
Anthony Straine,
Junior Data Scientist

Christopher Logan Ortiz,
Junior Data Scientist

## Description
Predict the market value of single unit properties using properties that were sold in May and June of 2017.

## Summary
_In Progress_

## Data Dictionary
| Feature | Definition | Data Type | 
| --- | --- | --- |
| id | row index number, range: 0 - 2985216 | int64 |
| parcelid | Unique numeric id assigned to each property: 10711725 - 169601949  | int64 |
| bathroomcnt | Number of bathrooms a property has: 0 - 32 | float64 | 
| bedroomcnt | Number of bedrooms a property has: 0 - 25  | float64 |
| calculatedbathnbr | Duplicate column of `bathroomcnt` : 1 - 32 | float64 |
| calculatedfinishedsquarefeet | Number of square feet of the property: 1 - 952576 | float64 |
| finishedsquarefeet12 | Duplicate column of `calculatedfinishedsquarefeet` : 1 - 952576  | float64 |
| fips | Federal Information Processing System [(FIPS)](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) Codes for States and Counties
Five digit numeric value that uniquely identifies geographic areas. Five digit number of which the 
first two are the FIPS code of the state to which the county belongs. Leading 0 is removed from the data: 6011=Colusa County, 6037=Los Angeles County, 6111=Ventura County | float64 |
| fullbathcnt | Number of full bathrooms a property has: 1 - 32 | float64 |
| latitude| Update: US Survey Foot? | float64 |
| longitude | Update: US Survey Foot? | float64 |
| lotsizesquarefeet |The land the property occupies in squared feet : 100 - 371000512 | float64 |
| propertycountylandusecode |  | object |
| propertylandusetypeid |  | float64 |
| rawcensustractandblock |  | float64 |
| regionidcity |  | float64 |
| regionidcounty |  | float64 |
| regionidzip |  | float64 |
| roomcnt |  | float64 |
| yearbuilt | Year the property was built | float64 |
| structuretaxvaluedollarcnt |  | float64 |
| taxvaluedollarcnt |  | float64 |
| assessmentyear |  | float64 |
| landtaxvaluedollarcnt |  | float64 |
| taxamount |  | float64 |
| censustractandblock |  | float64 |
 
| Target | Definition | Data Type |
| --- | --- | --- |
| Target 1 | Definition 1 | Data Type|

## Project Organization
```
├── README.md               <- The top-level README for developers using this project.
│
├── data                    <- All of the data for the project
│   ├── modeling            <- The prepared, processed and split datasets for modeling.
│   ├── prepared            <- The prepared datasets for exploration
│   └── raw                 <- The original, immutable data
│
├── main.py                 <- The main python script that calls all src scripts
│
├── mvp.ipynb               <- The main notebook for the project
│
├── src                     <- The source code for use in this project
│   ├── __init__.py         <- Makes src a Python module
│   ├── acquire.py          <- The script to download or generate data and store it in
│   │                          data/raw/
│   ├── explore.py          <- The script for creating any visuals that need to be stored
│   │                          in visuals/generated_graphics/
│   ├── model.py            <- The script for preprocessing, modeling, and interpreting
│   └── prepare.py          <- The script for preparing the raw data and storing it in
│                              data/prepared/
│
└── visuals                 <- All project visuals
    ├── external_visuals    <- Visuals brought from outside the project
    ├── generated_graphics  <- Visuals generated from the project
    └── presentation        <- A copy of your presentation
```

## Requirements
- numpy >= 1.1.2
- pandas >= 1.18.1
- matplotlib >= 3.3.1
- seaborn >= 0.11.0

## Setup
---
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

How to reach Chris
- [@Promeos42](https://twitter.com/Promeos42)
- 📫 christopher.logan.ortiz@gmail.com