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
For first steps in EDA I used the Pandas functions .info() and .describe(). The most noticeable issue that would have to be addressed is that the minimum value for a number of features were -99999. This seems to have been used as a placeholder, so the first bit of cleaning was to convert all of the placeholder values to NaN. Once this was done, I counted the number of NaN entries by feature to see which features would be viable. Many of the latter features had NaN counts of about 150,000 in a total of 209,000 entries. Looking through the feature names, I compared the number of NaN values with the assumed relevance of the feature to narrow down the feature list from 105 to 23. Using .describe() again on the chosen features, I started to look at the outliers. Many of the outliers were larger hospitals that had more beds. Not wanting to throw away potentially valuable data at this stage, I decided not to remove these. I did however remove entries that had incorrect entries (some smaller hospitals had bed counts in the 100,000s).

### 3. Visualization
The first step in visualizing the data was to pick out some features that I felt would be most relevant to the dataset. The first choice was to compare the bed occupancy rate to the number of suspected and confirmed COVID-19 patients.

![Bed Occupancy and COVID Patients](/img/bedsvscovid.png)

We can see from this plot that as the percentage of COVID patients increase, there is an increase in the number of inpatient bed being used. This goes with the intuition that during a pandemic, as more people are getting sick the more hospital beds are being used. I decided I needed to look at different features to see if they would tell a different story.
After some more plotting with limited success, I decided to revisit the bed use, but look at it on a smaller scale. I plotted the number of occupied beds against the total number of beds for a couple of communities, and this is what I found:

![Bed Occupancy](/img/bedusezip1.png) ![Bed Occupancy](/img/bedusezip2.png)

I had been thinking about the total number of beds available as a static number, this if it moved it would not change much. But it the plots above, we can see that the total number of beds is a much more fluid number. Using just the sum of beds, either in use or the total amount, will not be as relevant as I had hoped. Taking this a step further, something that could still be of use would be the rate of occupancy. For the next plot, I decided to use the rate of inpatient beds compared to the rate of ICU beds.

![Adult Bed Occupancy Rate](/img/adultbeduse.png)

The graph made me stop and pause. The rates for ICU and inpatient beds seemed to follow a similar path until after the start of the new year. Though the line plots were similar, it seemed that the inpatient bed rate was slightly higher than the ICU rate; but the real questions are: is the difference statistically significant, and what does it mean if the difference is significantly different? At this point I decided to form a hypothesis.

### 4. Forming a Hypothesis
From my observations of the graph above, I wanted to test the hypothesis that one of the rates is greater than the other. Before I can start testing, though, I needed to formalize a Null Hypothesis, as well as an Alternate Hypothesis. I will also need to make an assumption about the variables being Independent and Identically Distributed. Since the occupancy rates are coming from the same hospitals, it is extremely unlikely that the vairables are truly independent. For the sake of testing though, we will assume that the variables are IID.

**Null Hypothesis**
During Covid, the average occupancy rate for inpatient beds is the same as the average occupancy rate for ICU beds

**Alternate Hypothesis**
During Covid, the average occupancy rate for inpatient beds is greater than the average occupancy rate for ICU beds

Now that the we have our hypothesis, we need to determine our Alpha value as well as ensure that our test has enough statistical power. There is no compelling argument to use an Alpha value other than the standard 5%, so we will use an Alpha of 0.05. For the power calculation, I used a power calculating function from the Stats Models library. A statistical power level of greater than 80% is considered to be sufficient. Our power value was over 99%, so we have enough power to proceed with our test.

### 5. Hypothesis Testing
![Mann-Whitney Signed Rank Test](/img/mannwhitney.png)

### 6. Drawing Conclusions


### 7. Links to Sources



Link to Data Source: 
https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/uqq2-txqb



Institute for Health Metrics and Evaluation
http://www.healthdata.org/sites/default/files/files/Projects/COVID/briefing_US_2020.12.04_.pdf
