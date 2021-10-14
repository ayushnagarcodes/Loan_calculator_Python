# It is a program that can calculate:
# 1. number of monthly payments
# 2. annuity monthly payment amount which is fixed during the whole loan term
# 3. loan principal
import math
user_input = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')
if user_input == 'n':
    loan_principal = float(input('Enter the loan principal: '))
    annuity_monthly_payment = float(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))
    i = loan_interest / (12 * 100)
    n_monthly_payments = math.log(annuity_monthly_payment / (annuity_monthly_payment - i * loan_principal), 1 + i)
    years = (math.ceil(n_monthly_payments)) // 12
    months = (math.ceil(n_monthly_payments)) % 12
    output = f'It will take {years} years and {months} months to repay this loan!'
    if years == 1:
        print(output.replace('years', 'year'))
    elif years == 0:
        print(output.replace(f' {years} years and', ''))
    if months == 1:
        print(output.replace('months', 'month'))
    elif months == 0:
        print(print(output.replace(f' and {months} months', '')))
    else:
        print(output)
elif user_input == 'a':
    loan_principal = float(input('Enter the loan principal: '))
    n_monthly_payments = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    i = loan_interest / (12 * 100)
    annuity_monthly_payment = loan_principal * ((i * (1 + i) ** n_monthly_payments) / ((1 + i) ** n_monthly_payments - 1))
    print(f'Your monthly payment = {math.ceil(annuity_monthly_payment)}!')
elif user_input == 'p':
    annuity_monthly_payment = float(input('Enter the annuity payment: '))
    n_monthly_payments = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    i = loan_interest / (12 * 100)
    loan_principal = annuity_monthly_payment / ((i * (1 + i) ** n_monthly_payments) / ((1 + i) ** n_monthly_payments - 1))
    print(f'Your loan principal = {round(loan_principal)}!')