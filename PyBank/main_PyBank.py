# HW3-# PyBank

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
Total_ProfitLoss = 0

MaxProfit = 0
MinProfit = 0

AvgChngPL = 0

FirstValue = 0
CurrentValue = 0

G_Incr_P = 0
G_Decr_L = 0

ChangeList = []

# path = "C:\Users\momina\python-challenge\PyBank"
#file = 'python-challenge/PyBank/budget_data.csv'
budget_file = ('budget_data.csv')

with open(budget_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # This skips the first row of the CSV file - Header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        # The total number of months included in the dataset
        Total_Months = int(sum(1 for row in open(budget_file,"r",encoding="utf-8")) -1)
        print(Total_Months)
    
        # The net total amount of "Profit/Losses" over the entire period
        Total_ProfitLoss += int(row[1])
        print(Total_ProfitLoss)

        # The average of the changes in "Profit/Losses" over the entire period
        FirstValue += int(row[1])
        CurrentValue += int(row[1]) - int(FirstValue)
        print(CurrentValue)

        # Find the change in profits
        ChangeList.append[CurrentValue]
            
    for change in ChangeList:
        # Find out whether greatest increase/greatest decrease
        # List manipulation of some sort here
        if CurrentValue > G_Incr_P:
            G_Incr_P = CurrentValue
            print(FirstValue)
            print(CurrentValue)
            print(G_Incr_P)
        elif CurrentValue  < G_Decr_L:
            G_Decr_L = CurrentValue
            print(FirstValue)
            print(CurrentValue)
            print(G_Decr_L)

