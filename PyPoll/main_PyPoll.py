# ==================================================================================
# HW3- Python Homework
# ===================================================================================
# Python-Challenge: PyPoll
#
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# ===================================================================================

  # This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

# path = "C:\Users\momina\python-challenge\PyPoll"
# file = 'python-challenge/PyPoll/election_data.csv'
# 3 columns: `Voter ID`, `County`, and `Candidate`
# CSV reader specifies delimiter and variable that holds contents


election_file = ('election_data.csv')

votes_count = 0
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # This skips the first row of the CSV file - Header
    csv_header = next(csvreader)

    # The total number of votes cast = Total number of rows in csv file
    # Read each row of data after the header
    row_count = int(sum(1 for row in open(election_file,"r",encoding="utf-8")) -1)
    print("Total Records in file : ", votes_count)

# Candidate = []
# csvreader = csv.reader(csvfile, delimiter=',') 
# # This skips the first row of the CSV file - Header
# csv_header = next(csvreader)
# for row in csvreader:
#     if row[1] not in Candidate:
#         Candidate.append(row[2])    

# print(Candidate)        

# print("Election Results: ")
# print("----------------  ")
# print("Total Votes     : ", votes_count)
# print("----------------" )
# print("Khan            : ", )     # 63.000% (2218231)
# print("Correy          : ", )     # 20.000% (704200)
# print("Li              : ", )     # 14.000% (492940)
# print("O'Tooley        : ", )     #  3.000% (105630)
# print("----------------  ")
# print("Winner: Khan
# print("----------------  ")