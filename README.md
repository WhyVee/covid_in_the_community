# COVID in the Community
## Hospital Bed Occupancy Rates During the COVID-19 Pandemic

### Summary
COVID-19 has had a large impact across communities all over the United States. By observing data provided by the Department of Health and Human Services, we will attempt to find some commonality between some of the features in the dataset. If we can find commonality, we may be able to form a hypothesis that can not only provide us with interesting information but have a real-world application as well.

### Contents:
1. Reading in the Data Source
2. Initial EDA and Cleaning
3. Visualization
4. Forming a Hypothesis
5. Hypothesis Testing
6. Drawing Conclusions
7. Links to Sources

### 1. Reading in the Data Source
Description of Data:
CSV format, 105 Features, 209463 Entries; data types: bool(1), float64(71), int64(23), object(10); memory usage: 166.4+ MB
Important Features: Hospital name, city, zip code, total beds (7 day sum), total inpatient beds (7 day sum), inpatient beds used (7 day sum), ICU beds used (7 day sum), total ICU beds (7 day sum), as well as suspected COVID admissions sum for 0 to 80+ days, in 7 day increments.

Importing Data:
Since the data is in the CSV format, I was able to use Pandas to read the data into a Data Frame. From this point I was able to use Pandas functions to perform initial EDA as well as some initial cleaning.

### 2. Initial EDA and Cleaning

Link to Data Source: 
https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/uqq2-txqb



Institute for Health Metrics and Evaluation
http://www.healthdata.org/sites/default/files/files/Projects/COVID/briefing_US_2020.12.04_.pdf
