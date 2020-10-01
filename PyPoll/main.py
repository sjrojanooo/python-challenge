import os
import csv

#Create path to collect data from the resource folder
py_poll = os.path.join('poll_analysis.csv')

#Declaring my variables
total_votes = 0
khan = 0
correy = 0
li = 0
ot = 0

#Reading in the csv File that we are working with
with open(py_poll) as csvfile:

    #split the data with comma delimiter
    reader = csv.reader(csvfile, delimiter=",")

    #Telling the program to skip the header so that we only iterate through
    #the values within the data set
    header = next(reader)

    #for loop that is used to iterate through each row
    for row in reader:

        #Counter variable is used to count through the unique Voter ID ballots
        #This will give us the grand total of votes within the data set
        total_votes += 1

        #if statement that will count the unique name values in the given data set
        #counters will hold the value of each vote for the specific candidate
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            ot += 1

    #calculating the percentage of votes that each candidate recieved
    #I am also formatting them in percentage format to the specific decimal place
    khan_perc = "{:.2%}".format((khan/total_votes))
    correy_perc = "{:.2%}".format((correy/total_votes))
    li_perc = "{:.2%}".format((li / total_votes))
    ot_perc = "{:.2%}".format((ot/total_votes))

    #making a dictionary for the polling results for each candidate
    candidate = ["Khan", "Correy","Li","O'Tooley"]
    poll_results = [khan, correy, li, ot]

    candidate_votes = dict(zip(candidate, poll_results))
    key = max(candidate_votes, key=candidate_votes.get)

    print(f"Election Results")
    print(f"------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------")
    print(f"Khan: {khan_perc} {khan}")
    print(f"Correy:  {correy_perc} {correy}")
    print(f"Li:  {li_perc} {li}")
    print(f"O'Tooley:  {ot_perc} {ot}")
    print(f"------------------------")
    print(f"Winner: {key}")
    print(f"------------------------")
    print(f"\n\n")



output_poll_file = os.path.join("Poll_Results.csv")

#opening the output file
with open(output_poll_file, "w") as writer:

    #printing out the cleaned up csv file for the user
    writer.write(f"Election Results")
    writer.write(f"\n")
    writer.write(f"------------------------")
    writer.write(f"\n")
    writer.write(f"Total Votes: {total_votes}")
    writer.write(f"\n")
    writer.write(f"------------------------")
    writer.write(f"\n")
    writer.write(f"Khan:     {khan_perc}  ({khan})")
    writer.write(f"\n")
    writer.write(f"Correy:   {correy_perc}   ({correy})")
    writer.write(f"\n")
    writer.write(f"Li:       {li_perc}   ({li})")
    writer.write(f"\n")
    writer.write(f"O'Tooley:  {ot_perc}   ({ot})")
    writer.write(f"\n")
    writer.write(f"------------------------")
    writer.write(f"\n")
    writer.write(f"Winner: {key}")
    writer.write(f"\n")
    writer.write(f"------------------------")

