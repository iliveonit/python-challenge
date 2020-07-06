# ==================================================================================
# HW3: Python-Challenge: PyPoll
# ===================================================================================

  # This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

# path = "C:\Users\momina\python-challenge\PyPoll"
# file = 'python-challenge/PyPoll/election_data.csv'
# 3 columns: `Voter ID`, `County`, and `Candidate`
# CSV reader specifies delimiter and variable that holds contents
# csvpath = os.path.join('.','election_data.csv')

election_file = ('election_data.csv')

total_votes = 0
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # This skips the first row of the CSV file - Header
    csv_header = next(csvreader)
    print(csv_header)
    # --------------------------------------------------------------------
    # The total number of votes cast = Total number of rows in csv file
    # --------------------------------------------------------------------
    # Read each row of data after the header
    total_votes = int(sum(1 for row in open(election_file,"r",encoding="utf-8")) -1)
    print("Total Records in file : ", total_votes)

    # --------------------------------------------------------------------
    # A complete list of candidates who received votes
    # --------------------------------------------------------------------
    Candidate = []

    for row in csvreader:
        if row[2] not in Candidate:
            Candidate.append(row[2])    
            
    print(Candidate) 

# --------------------------------------------------------------------
# The percentage of votes each candidate won
# --------------------------------------------------------------------
# def print_VotePct(candidate,votes,pct)
#     var_candidate = 
#     var_votes =
#     var_pct = (var_votes / total_votes) * 100

# --------------------------------------------------------------------
# The total number of votes each candidate won
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# The winner of the election based on popular vote.
# --------------------------------------------------------------------

       

print("Election Results: ")
print("----------------  ")
print("Total Votes     : ", total_votes)
print("----------------" )
print("Complete list of candidates who received votes: ")
print("-----------------------------------------------" )
print(Candidate[0])
print(Candidate[1])
print(Candidate[2])
print(Candidate[3])
print("-----------------------------------------------" )
# print("Khan            : ", )     # 63.000% (2218231)
# print("Correy          : ", )     # 20.000% (704200)
# print("Li              : ", )     # 14.000% (492940)
# print("O'Tooley        : ", )     #  3.000% (105630)
# print("----------------  ")
# print("Winner: Khan
# print("----------------  ")