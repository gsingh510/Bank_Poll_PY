import os
import csv
import pandas as pd
# variables
Candidates =[]
c_votes = {}

total_votes = 0
winner_count = 0
election_winner = ""
#importing file
#finding header of csv file and printing it
#set up of table that will print in terminal with outputs
with open ("/Users/gagans/Desktop/python-challenge/Main_Resources/PyPoll/Resources/election_data.csv","r") as PD:
    lines = PD.readlines()
    sum_of_votes = (len(lines) -1)
    print("  Election Results")
    print("______________________________")
    print(f"  Total Votes: {sum_of_votes}")
    print("______________________________")
    print("Candidate: Percentage and Votes")
    print("")

#reopned csv file to run calcuations to find the election results
#for loop to add all votes for each candidate
with open ("/Users/gagans/Desktop/python-challenge/Main_Resources/PyPoll/Resources/election_data.csv","r") as polldata:
    csvreader = csv.DictReader(polldata)

    for row in csvreader:

        total_votes += 1 

        Candidate = row["Candidate"]
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            c_votes[Candidate] = 1

        c_votes[Candidate] = c_votes[Candidate] + 1

#for loop to find the winner of the election
    for candidate in c_votes:
        votes = c_votes[candidate]
        vote_percentage = (float(votes)/float(total_votes)) *100
        if (votes > winner_count):
            winner_count = votes
            election_winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output) 
    win_summary = {election_winner} 
    winner = (f"Winner of election: {win_summary}")
    print (winner)
#output data table to a txt file 
with open ("/Users/gagans/Desktop/python-challenge/Main_Resources/Output/Poll_results", "x") as Election_results:
    Election_results.write("  Election Results\n")
    Election_results.write("______________________________\n")
    Election_results.write(f"  Total Votes: {sum_of_votes}\n")
    Election_results.write("______________________________\n")
    Election_results.write("Candidate: Percentage and Votes\n")
    Election_results.write(voter_output)
    Election_results.write("\n")       
    Election_results.write(winner)
   
   





         





