# ==================================================================================
# HW3: Python-Challenge: PyPoll
# ===================================================================================

  # This will allow us to create file paths across operating systems
import os

# Modules for reading CSV files
import csv

# --------------------------------------------------------------------------
# Input file 

# path = "C:\Users\momina\python-challenge\PyPoll"
# file = 'python-challenge/PyPoll/election_data.csv'
# 3 columns: `Voter ID`, `County`, and `Candidate`
# CSV reader specifies delimiter and variable that holds contents
# csvpath = os.path.join('.','election_data.csv')

election_file = ('election_data.csv')

# --------------------------------------------------------------------------

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
    Votes = []
    
    for row in csvreader:
        if row[2] not in Candidate:
            Candidate.append(row[2])
    print(Candidate)

    for row in csvreader:
        Votes = 0
        if row[2] in Candidate:
            Votes = Votes + 1
    print ("Votes : ", Votes)

    # votes = 0
    # for row in csvreader:
    #     for name in Candidate:
    #       votes = 0
    #       if row[2] == Candidate:
    #           votes.append(row[0])
    #       print(Candidate, votes) 

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
print("The percentage of votes each candidate won:")
print("Khan            : ", )     # 63.000% (2218231)
print("Correy          : ", )     # 20.000% (704200)
print("Li              : ", )     # 14.000% (492940)
print("O'Tooley        : ", )     #  3.000% (105630)
print("----------------  ")
print("Winner: Khan")
print("----------------  ")

# --------------------------------------------------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Specify the file to write to
output_path = os.path.join('.','PyPoll_Results.txt')

# Open the file using "write" mode; with variable to hold content
# with open(output_path, 'w') as csvfile:
file = open(output_path, 'w')
file.write("Election Results: ")
file.write("----------------  ")
file.write("Total Votes     : " % total_votes)
file.write("----------------" )
file.write("Complete list of candidates who received votes: ")
file.write("-----------------------------------------------" )
file.write(Candidate[0])
file.write(Candidate[1])
file.write(Candidate[2])
file.write(Candidate[3])
file.write("-----------------------------------------------" )
file.write("The percentage of votes each candidate won:")
file.write("Khan            : ")     # 63.000% (2218231)
file.write("Correy          : " )     # 20.000% (704200)
file.write("Li              : " )     # 14.000% (492940)
file.write("O'Tooley        : " )     #  3.000% (105630)
file.write("----------------  ")
file.write("Winner: Khan")
file.write("----------------  ")
file.close()

# ---------------------------------------------------------------------------
# End of code
# ---------------------------------------------------------------------------
