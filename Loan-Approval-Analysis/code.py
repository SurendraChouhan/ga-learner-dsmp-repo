# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
banks = pd.DataFrame(bank.drop(columns = 'Loan_ID'))

print(banks.isnull().sum())

bank_mode = banks.mode()
print(bank_mode)

banks = pd.DataFrame(banks.fillna('bank_mode'))

print(banks)
#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks,index = ['Gender','Married','Self_Employed'],values = 'LoanAmount', aggfunc = np.mean)

print(avg_loan_amount)

# code ends here



# --------------
# code starts here

a = banks.Self_Employed == 'Yes'
b = banks.Loan_Status == 'Y'
c = banks.Self_Employed == 'No'

loan_approved_se = len(banks[a & b])
print(loan_approved_se)

loan_approved_nse = len(banks[c & b])
print(loan_approved_nse)

percentage_se = loan_approved_se/614 * 100
print(percentage_se)

percentage_nse = loan_approved_nse * 100 / 614
print(percentage_nse)

#percentage_nse = (c & b).value_counts(normalize=True).mul(100).astype(str)+'%'
#print(percentage_nse)
#code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
print(loan_term)

a = loan_term >= 25
print(len(a))

big_loan_term = len(banks[a])
print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


