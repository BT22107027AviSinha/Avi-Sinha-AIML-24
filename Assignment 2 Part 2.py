import pandas as pd 

# Load the salary data
salary_data = pd.read_csv('Salaries.csv')

# Display the first few rows of the dataset
print("Top rows of the dataset:")
print(salary_data.head())

# Display basic information about the dataset
print("\nOverview of the dataset:")
print(salary_data.info())

# Calculate the average base payment
avg_base_payment = salary_data['BasePay'].mean()
print("\nAverage Base Payment:", avg_base_payment)

# Find the highest overtime payment
max_overtime_payment = salary_data['OvertimePay'].max()
print("\nMaximum Overtime Payment:", max_overtime_payment)

# Identify the job title of a specific individual (JOSEPH DRISCOLL)
driscoll_job_title = salary_data[salary_data['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].iloc[0]
print("\nJob title of JOSEPH DRISCOLL:", driscoll_job_title)

# Determine the total pay including benefits for JOSEPH DRISCOLL
driscoll_total_pay = salary_data[salary_data['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].iloc[0]
print("\nTotal pay including benefits for JOSEPH DRISCOLL:", driscoll_total_pay)

# Find the name of the highest-paid individual (including benefits)
highest_paid_individual = salary_data.loc[salary_data['TotalPayBenefits'].idxmax()]['EmployeeName']
print("\nName of highest-paid individual (including benefits):", highest_paid_individual)

# Identify the name of the lowest-paid individual (including benefits)
lowest_paid_individual = salary_data.loc[salary_data['TotalPayBenefits'].idxmin()]['EmployeeName']
print("\nName of lowest-paid individual (including benefits):", lowest_paid_individual)

# Calculate the average base payment per year for the years 2011-2014
avg_base_payment_per_year = salary_data.groupby('Year')['BasePay'].mean()
print("\nAverage Base Payment per year:")
print(avg_base_payment_per_year)

# Determine the number of unique job titles
unique_job_titles_count = salary_data['JobTitle'].nunique()
print("\nNumber of unique job titles:", unique_job_titles_count)

# Identify the top 5 most common job titles
top_5_common_jobs = salary_data['JobTitle'].value_counts().head()
print("\nTop 5 most common job titles:")
print(top_5_common_jobs)

# Count the number of job titles represented by only one person in 2013
unique_job_titles_2013_count = sum(salary_data[salary_data['Year'] == 2013]['JobTitle'].value_counts() == 1)
print("\nNumber of job titles represented by only one person in 2013:", unique_job_titles_2013_count)

# Count the number of people with the word 'Chief' in their job title
chief_count = salary_data[salary_data['JobTitle'].str.contains('Chief', case=False)]['JobTitle'].count()
print("\nNumber of people with the word 'Chief' in their job title:", chief_count)

# Check if there is a correlation between the length of the job title string and salary
salary_data['TitleLength'] = salary_data['JobTitle'].apply(len)
correlation_length_salary = salary_data[['TitleLength', 'TotalPayBenefits']].corr().iloc[0, 1]
print("\nCorrelation between length of job title string and salary:", correlation_length_salary)
