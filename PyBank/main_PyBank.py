# ===================================================================================
# HW3- Python Homework
# ===================================================================================

# This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

MaxProfit = 0
MinProfit = 0



ChangeList = []

profit_array = []
loss_array = []

# path = "C:\users\momina\python-challenge\PyBank\budget_data.csv"
budget_file = ('budget_data.csv')

with open(budget_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # This skips the first row of the CSV file - Header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # --------------------------------------------------------------------------
    # The total number of months included in the dataset
    # Read each row of data after the header
    Total_Months = 0
    Total_Months = int(sum(1 for row in open(budget_file,"r",encoding="utf-8")) -1)
    print("Financial Analysis of the dataset:")
    print("----------------------------------")
    print("Total Months in the dataset      : ", Total_Months)

# --------------------------------------------------------------------------
# The net total amount of "Profit/Losses" over the entire period
cr = csv.reader(open(budget_file,"r"))
csv_header = next(cr) # to skip the header 

# Total_ProfitLoss
Total_PL = 0
for row in cr:
    #print(row[1])
    Total_PL += int(row[1])

    #Total_ProfitLoss = int(sum(row[1] for row in open(budget_file,"r",encoding="utf-8")) -1)
    #print("Total: ", Total_PL)
print("Net Profit/Losses for the period : ", Total_PL)

# The average of the changes in "Profit/Losses" over the entire period
AvgChngPL = 0
AvgChngPL = Total_PL / Total_Months
print("Average changes in Profit/Losses : ", AvgChngPL)

# --------------------------------------------------------------------------

g_incr = 0
g_decr = 0

with open(budget_file) as FinAnalysis:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

for row in reader:

# Track number of rows
  if first_value_YN is False:
    first_value = row[1]
    first_value_YN is True
  else:
    # Find the change in profits
    curr_change = row[1] - first_value
    change_list.append(curr_change)

    for change in change_list:
      # Find out the g_incr/g_decr

      if curr_change > g_incr
        g_incr = curr_change
      else 
        curr_change < g_decr
 


# Get the previous value

# Subtract the previous value from the current value

# Do comparison-additions

# --------------------------------------------------------------------------
# End of Code
# --------------------------------------------------------------------------