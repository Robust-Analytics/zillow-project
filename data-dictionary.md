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

