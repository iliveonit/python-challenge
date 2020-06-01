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
    
    # The total number of months included in the dataset
    # Read each row of data after the header
    Total_Months = 0
    Total_Months = int(sum(1 for row in open(budget_file,"r",encoding="utf-8")) -1)
    # print("Financial Analysis of the dataset:")
    # print("----------------------------------")
    # print("Total Months in the dataset      : ", Total_Months)

# The net total amount of "Profit/Losses" over the entire period
cr = csv.reader(open(budget_file,"r"))
csv_header = next(cr) # to skip the header 

Total_ProfitLoss = 0
for row in cr:
    #print(row[1])
    Total_ProfitLoss += int(row[1])

Total_PL = Total_ProfitLoss
#Total_ProfitLoss = int(sum(row[1] for row in open(budget_file,"r",encoding="utf-8")) -1)
#print("Total: ", Total_ProfitLoss)
# print("Net Profit/Losses for the period : ", Total_PL)
 
cr = csv.reader(open(budget_file,"r"))
csv_header = next(cr) # to skip the header 

MaxProfit = 0
MinProfit = 0

G_Incr_P = 0
G_Decr_L = 0

ChangeList = []
profits_array = []
losses_array = []

for row in cr:
    if (budget_file[1] < 0):
        losses_array.append(budget_file[1])

    else:
        profits_array.append(budget_file[1])


# The average of the changes in "Profit/Losses" over the entire period
AvgChngPL = 0
AvgChngPL = Total_PL / Total_Months
print("Average changes in Profit/Losses : ", AvgChngPL)

   

    

    #     FirstValue = 0
    #     CurrentValue = 0
    #     FirstValue = FirstValue + (row[1])
    #     CurrentValue += int(row[1]) - int(FirstValue)
    #     print(CurrentValue)

    #     # Find the change in profits
    #     ChangeList.append[CurrentValue]
            
    # for change in ChangeList:
    #     # Find out whether greatest increase/greatest decrease
    #     # List manipulation of some sort here
    #     if CurrentValue > G_Incr_P:
    #         G_Incr_P = CurrentValue
    #         print(FirstValue)
    #         print(CurrentValue)
    #         print(G_Incr_P)
    #     elif CurrentValue  < G_Decr_L:
    #         G_Decr_L = CurrentValue
    #         print(FirstValue)
    #         print(CurrentValue)
    #         print(G_Decr_L)


max_profit = max(profits_array) - min(profits_array)
max_loss = max(losses_array) - min(losses_array)

# The greatest increase in profits (date and amount) over the entire period
max_profit = max(profits_array) - min(profits_array)

# The greatest decrease in losses (date and amount) over the entire period
max_loss = max(losses_array) - min(losses_array)

# In addition, your final script should both print the analysis -
# to the terminal


print("Financial Analysis of the dataset:")
print("----------------------------------")
print("Total Months in the dataset      : ", Total_Months)
print("Net Profit/Losses for the period : ", Total_PL)
print("Average changes in Profit/Losses : ", AvgChngPL)
print("Greatest Increase in Profits     : ",   )    # Feb-2012 ($1926159)
print("Greatest Decrease in Profits     : ",   )    # Sep-2013 ($-2196167)

# and export a text file with the results
Results_file = 'Finanical_Analysis_Results.txt'

# 2. Creating the Text_IO_Wrapper: 
#    Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(Results_file, 'w') as text:   # text is the wrapper

  # 3. Creating the writer object: 
csvwriter = csv.writer(csvfile, delimiter=",")

  # Write a new row
csvwriter.writerow(listobject)

with open("Output.txt", "w") as text_file:
text_file.close()
