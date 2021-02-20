import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

        
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
        
    candidates = {}
    total_votes = 0
    max_votes = 0
    name = "does not exist"

    for row in csvreader:
#        print(row)

        total_votes += 1

        candidate = row[2]
        candidates[candidate] = 1 + candidates.get(candidate,0)


    result = ("Election Results\n")
    result+=("----------------------\n")
    result+=(f"Total Votes: {total_votes}\n")
    result+=("----------------------\n")

    for candidate, votes in candidates.items():

        result+=(f"{candidate}: {round(votes*100/total_votes,3):.3f}% ({votes})\n")
        if votes > max_votes:
            max_votes = votes
            name = candidate
    result+=("---------------------\n")
    result+=(f"Winner: {name}\n")
    result+=("---------------------\n")
    result+=("---\n")

    print(result)

    with open("result.txt", "w") as text_file:
        text_file.write(result)