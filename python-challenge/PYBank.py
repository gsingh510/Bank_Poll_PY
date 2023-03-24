import os
import csv
import pandas as pd

#variables 
profit = []
months = []
change_in_revenue = []

# Open csv file and print total months in data sheet
# Start layout of table
with open("/Users/gagans/Desktop/python-challenge/Main_Resources/PyBank/Resources/budget_data.csv","r") as budgetdata:
    lines = budgetdata.readlines()
    Sum_of_months = len(lines)

# Reopen csv file and read header in order to print it
with open("/Users/gagans/Desktop/python-challenge/Main_Resources/PyBank/Resources/budget_data.csv","r") as budgetdata:
    
    Bankcsv = csv.reader(budgetdata, delimiter=",")
    budgetdata_header = next(budgetdata)
    print(f"Header: {budgetdata_header}")

# Read each row that is after the header
    for rows in Bankcsv:
        profit.append(int(rows[1]))
        months.append(rows[0])


    for x in range(1, len(profit)):
        change_in_revenue.append((int(profit[x]) - int(profit[x-1])))
    
    # Average change in revenue
    average_of_revenue = sum(change_in_revenue) / len(change_in_revenue)


    # Calculate highest increase in revenue
    highest_increase = max(change_in_revenue)
    # Calculate highest decrease in revenue
    highest_decrease = min(change_in_revenue)

#Create table in terminal and print the results of calculations. 

print("Financial Analysis\n")
print("___________________\n")
print(f"Total Months: {Sum_of_months}\n")
print(f"Total Profit: $ {sum(profit)}\n")
print(f"Average Change: $ {average_of_revenue}\n")
print(f"Greatest Increase In Profits: $ {highest_increase}\n")
print(f"Greatest Decrease In Profits: $ {highest_decrease}\n")

# Output to file. 

with open("/Users/gagans/Desktop/python-challenge/Main_Resources/Output/Bank_results","x") as Bankresults:
    Bankresults.write("Financial Analysis\n")
    Bankresults.write("___________________\n")
    Bankresults.write(f"Total Months: {Sum_of_months}\n")
    Bankresults.write(f"Total Profit: $ {sum(profit)}\n")
    Bankresults.write(f"Average Change: $ {average_of_revenue}\n")
    Bankresults.write(f"Greatest Increase In Profits: $ {highest_increase}\n")
    Bankresults.write(f"Greatest Decrease In Profits: $ {highest_decrease}\n")



