import pandas as pd

def general_clean(df, chosen_features, hyp_test_features):
    '''
    Performs general cleanup of dataframe. Removed the most extreme outliers,
    replace placeholder values with NaN, trim the dataframe down to the features
    that were passed in. Create new column for "Percent Inpatient Beds". Format
    date and zip.
    =========
    Parameters:

        df: pandas dataframe

        chosen_features: list of the features that will be kept

        hyp_test_features: list of features used for hypothesis testing

    =========
    Returns:

        clean_df: pandas dataframe that has been cleaned
    '''
    #Some values were filled with -999999.0 rather than NaN
    clean_df = df.replace(-999999.0)
    clean_df['percent_inpatient_beds'] = clean_df['inpatient_beds_used_7_day_sum'] / clean_df['inpatient_beds_7_day_sum']
    clean_df = clean_df[chosen_features]
    
    for feature in hyp_test_features:
        clean_df = clean_df[clean_df[feature].notna()]

    clean_df = clean_df.astype({'zip': int})
    clean_df = clean_df.iloc[::-1].reset_index(drop=True)
    clean_df
    #Edge cases that were filled out incorrectly.
    drop_row_idx = [272, 102591, 69379]

    clean_df.drop(drop_row_idx, inplace=True)
    clean_df.drop(clean_df[clean_df['zip'] == 78205].index, inplace=True)

    clean_df = clean_df[clean_df['inpatient_beds_used_7_day_sum'] > 0]
    clean_df = clean_df[clean_df['inpatient_beds_7_day_sum'] > 0]
    clean_df.collection_week = pd.to_datetime(clean_df['collection_week'], format='%Y/%m/%d')

    return clean_df

def hyp_cleanup(df, feature_list):
    for feature in feature_list:
        df = df[df[feature].notna()]
        if not feature == 'icu_beds_used_7_day_sum':
            df = df[df[feature] > 0]

    df = df[df['total_icu_beds_7_day_sum'] > df['icu_beds_used_7_day_sum']]  

    return df




if __name__ == '__main__':
    filepath = '../data/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_Facility.csv'
    data = pd.read_csv(filepath)
    chosen_features_list = ['collection_week',
                            'hospital_name',
                            'zip',
                            'total_beds_7_day_sum',
                            'all_adult_hospital_beds_7_day_sum',
                            'all_adult_hospital_inpatient_beds_7_day_sum',
                            'inpatient_beds_used_7_day_sum',
                            'all_adult_hospital_inpatient_bed_occupied_7_day_sum',
                            'total_adult_patients_hospitalized_confirmed_and_suspected_covid_7_day_sum',
                            'total_adult_patients_hospitalized_confirmed_covid_7_day_sum',
                            'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_7_day_sum',
                            'total_pediatric_patients_hospitalized_confirmed_covid_7_day_sum',
                            'inpatient_beds_7_day_sum',
                            'total_icu_beds_7_day_sum',
                            'total_staffed_adult_icu_beds_7_day_sum',
                            'icu_beds_used_7_day_sum',
                            'staffed_adult_icu_bed_occupancy_7_day_sum',
                            'staffed_icu_adult_patients_confirmed_and_suspected_covid_7_day_sum',
                            'staffed_icu_adult_patients_confirmed_covid_7_day_sum',
                            'total_patients_hospitalized_confirmed_influenza_7_day_sum',
                            'icu_patients_confirmed_influenza_7_day_sum',
                            'total_patients_hospitalized_confirmed_influenza_and_covid_7_day_sum',
                            'percent_inpatient_beds']
    hyp_test_features = ['inpatient_beds_7_day_sum',
                         'inpatient_beds_used_7_day_sum',
                         'icu_beds_used_7_day_sum',
                         'total_icu_beds_7_day_sum',
                         'zip']

    clean_data = general_clean(data, chosen_features_list, hyp_test_features)

    print(clean_data.head())
