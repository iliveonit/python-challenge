# ===================================================================================
# HW3- Python Homework
# ===================================================================================

# This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

# --------------------------------------------------------------------------
# Input file 
# path = "C:\users\momina\python-challenge\PyBank\budget_data.csv"
budget_file = ('budget_data.csv')


# --------------------------------------------------------------------------
# Declaration: Variables 

MaxProfit = 0
MinProfit = 0

ChangeList = []

profit_array = []
loss_array = []

total_mnths = 0
net_PL = 0
avg_PL = 0
g_incr = 0
g_decr = 0

# --------------------------------------------------------------------------
# The total number of months included in the dataset

with open(budget_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # This skips the first row of the CSV file - Header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    # Read each row of data after the header
   
    total_mnths = int(sum(1 for row in open(budget_file,"r",encoding="utf-8")) -1)
    print("Financial Analysis of the dataset:")
    print("----------------------------------")
    print("Total Months included in the dataset : ", total_mnths)

# --------------------------------------------------------------------------
# The net total amount of "Profit/Losses" over the entire period
cr = csv.reader(open(budget_file,"r"))
csv_header = next(cr) # to skip the header 

# --------------------------------------------------------------------------
# Total_ProfitLoss

for row in cr:
    #print(row[1])
    Total_PL += int(row[1])

    #Total_ProfitLoss = int(sum(row[1] for row in open(budget_file,"r",encoding="utf-8")) -1)
    #print("Total: ", Total_PL)
print("Net Profit/Losses for the period : ", Total_PL)

# --------------------------------------------------------------------------
# The average of the changes in "Profit/Losses" over the entire period

avg_PL = net_PL / total_mnths
print("Average changes in Profit/Losses : ", avg_PL)

# --------------------------------------------------------------------------

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
    print("Value of curr_change: ", curr_change)
    print("Value of change_list: ", change_list)

    for change in change_list:
      # Find out the g_incr/g_decr

      if (curr_change > g_incr):
        g_incr = curr_change
        print("Value of g_incr: ", g_incr)
      else:
        curr_change < g_decr
        print("Value of g_decr: ", g_decr)
 
# ---------------------------------------------------------------------------
# Get the previous value
# Subtract the previous value from the current value
# Do comparison-additions

# ---------------------------------------------------------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Specify the file to write to
output_path = os.path.join('.','PyBank_Results.txt')

# Open the file using "write" mode; with variable to hold content
# with open(output_path, 'w') as csvfile:
file = open(output_path, 'w')
file.write("-----------------------------------------------" )
file.write("Financial Analysis: ")
file.write("-----------------------------------------------" )
file.write("Total Months included in the dataset : " % total_mnths)   # 86 Months
file.write("Net amount of Profit/Losses          : " % net_PL)        # $38382578
file.write("Average  Change of Profit/Losses     : " % avg_PL)        # $-2315.12
file.write("Greatest Increase in Profits         : " % g_incr)        # Feb-2012 ($1926159)
file.write("Greatest Decrease in Profits         : " % g_decr)        # Sep-2013 ($-2196167)
file.write("-----------------------------------------------" )
file.close()

# ---------------------------------------------------------------------------
# End of code
# ---------------------------------------------------------------------------