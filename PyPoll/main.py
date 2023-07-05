import csv
import os

# Path to collect data from the Resources folder
py_poll_data_csv = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_list = []
candidate_votes = {}
candidate_percent = {}
winner = ""
winner_votes = 0

# Read in the CSV file
with open(py_poll_data_csv, 'r') as csvfile:
            
     # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')
    
     # Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    
    # Iterate through the remaining rows
    for row in csv_reader:
    
        # Obtain total number of boats
        total_votes += 1
               
        # Obtain candidate name
        candidate = row[2]
    
        # Add candidate to list if not already in list
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] += 1

# print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# Calculate percentage of votes for each candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percent = (votes / total_votes) * 100
    candidate_percent[candidate] = percent

    # Determine winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

    # Print results
    print(f'{candidate}: {percent:.3f}% ({votes})')

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Export results to text file
output_path = os.path.join('Analysis', 'election_results.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = (votes / total_votes) * 100
        txtfile.write(f'{candidate}: {percent:.3f}% ({votes})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-------------------------\n')
    