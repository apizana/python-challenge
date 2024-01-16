import os
import csv

# set path for file to collect data
election_data = os.path.join("Resources", "election_data.csv")

# Set the output of the file
text_path="election_analysis.txt"

# Specify the file to write to
out_file = os.path.join("analysis", text_path)

# Total vote counter
total_votes = 0

#Candidates and votes
candidate_list = []
candidate_votes = {}

#Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(election_data) as election_data:
    file_reader = csv.reader(election_data, delimiter=",")
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add the candidate list.
        if candidate_name not in candidate_list:
            
            # Add the candidate name to the candidate list.
            candidate_list.append(candidate_name)
           
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to text file.
with open(text_path, "w") as text_file:
    
    # Print the total votes count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    text_file.write(election_results)
    
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.3f}% ({votes:})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        
        #  Save the candidate results to text file.
        text_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    # Print the winner candidate to the terminal.
    winner_candidate = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"              
        f"-------------------------\n")
    print(winner_candidate)
    
    # Save the winner candidate name to the text file.
    text_file.write(winner_candidate)

  
    