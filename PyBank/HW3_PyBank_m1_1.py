# HW3-Tasks
# PyBank

# #######################################################################################
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print 
# the analysis to the terminal and export a text file with the results.
# #######################################################################################

# This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

Total_Months = 0

# budget_data.csv
# path = "C:\Users\momina\python-challenge\PyBank"
budget_file = ('budget_data.csv')

with open(budget_file) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Total_Months = len(list(csvreader))
    Total_Months = int(sum(1 for row in open(budget_file,"r",encoding="utf-8")) -1)
    print(Total_Months)