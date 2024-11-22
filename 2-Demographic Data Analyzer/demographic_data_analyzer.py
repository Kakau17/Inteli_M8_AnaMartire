import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv('adult.data.csv', header=None, names=['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                                                           'marital-status', 'occupation', 'relationship', 'race', 'sex',
                                                           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])
    
    # 1. Number of each race represented in the dataset
    race_count = df['race'].value_counts(dropna=True).drop(labels='race', errors='ignore')

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].replace([None, float('inf')], pd.NA).dropna().astype(float).mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round((bachelors_count / total_count) * 100, 1)

    # 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) earning >50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = df[advanced_education & (df['salary'] == '>50K')].shape[0]
    higher_education_count = df[advanced_education].shape[0]
    percentage_higher_education_rich = round((higher_education_rich / higher_education_count) * 100, 1)

    # 5. Percentage of people without advanced education earning >50K
    non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = df[non_advanced_education & (df['salary'] == '>50K')].shape[0]
    lower_education_count = df[non_advanced_education].shape[0]
    percentage_lower_education_rich = round((lower_education_rich / lower_education_count) * 100, 1)

    # 6. Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work the minimum number of hours per week and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
    percentage_rich_min_workers = round((rich_min_workers / num_min_workers.shape[0]) * 100, 1)

    # 8. Country with the highest percentage of people that earn >50K
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_salary_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = round((country_salary_counts / country_counts * 100).max(), 1)

    # 9. Most popular occupation for those earning >50K in India
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupation.value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'percentage_rich_min_workers': percentage_rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Testing code - you can use this to see the results.
if __name__ == "__main__":
    results = demographic_data_analyzer()
    for key, value in results.items():
        print(f"{key}: {value}")