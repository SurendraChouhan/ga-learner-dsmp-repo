# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

loan_status = data['Loan_Status'].value_counts()

loan_status.plot(kind = 'bar')
plt.show()
#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
print(property_and_loan)

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

plt.xlabel('Property Area')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
print(education_and_loan)

education_and_loan.plot(kind = 'bar', stacked = True, figsize = (15,10))

plt.xlabel('Education Status')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)


# --------------
#Code starts here

cond = data['Education'] == 'Graduate'

graduate = data[cond]
print(graduate)

cond1 = data['Education'] == 'Not Graduate'

not_graduate = data[cond1]
print(not_graduate)

graduate.plot(kind = 'density', label = 'Graduate')

not_graduate.plot(kind = 'density', label = 'Not Graduate')

plt.show()
#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig , (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))

data.plot.scatter(x = 'ApplicantIncome', y = 'LoanAmount' , ax = ax_1)

data.plot.scatter(x = 'CoapplicantIncome', y = 'LoanAmount' , ax = ax_2)

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
print(data['TotalIncome'])

data.plot.scatter(x = 'TotalIncome', y = 'LoanAmount' , ax = ax_3)




