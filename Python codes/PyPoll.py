# Modules
import os
import csv
# Define variables
Candidates = {} # defined as Dictionary
# Set CSV path for pyPoll file
csvpath = os.path.join("..","Resources","election_data.csv")

# Create the looped row function:
def processRow(PollData):
    # Create dictionary of dictionary to collect all candidates and votes
    if PollData[2] not in Candidates:
        Candidates[PollData[2]] = {'vote':1}
    else: # Add +1 per vote
        '''
        vote_dict = Candidates[PollData[2]]
        total = vote_dict['vote']
        total +=1
        '''
        # A better way to write the above codes...
        vote = Candidates[PollData[2]]['vote'] + 1
        Candidates[PollData[2]] = {'vote': vote}

# Open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csv_header = next(csvreader)

    # Add up the total voters and run the function loop for each row
    TotalVotes = 0
    for row in csvreader:
        # print(row)
        TotalVotes += 1
        processRow(row)

    # Find the winner
    max = 0
    topCandidate = None
    for (k, v) in Candidates.items():
        v['percent'] = round((v['vote']/TotalVotes)*100,2)
        if v['vote'] > max:
            topCandidate = k
            max = v['vote']

# Results
with open("pyPoll_Final.txt", "w") as textfile:
    print("Election Results", file = textfile)
    print("-----------------------------", file = textfile)
    print(f"Total Votes: {TotalVotes}", file = textfile)
    print("-----------------------------", file = textfile)
    for (k, v) in Candidates.items():
        name = k
        print(f"{k}: {v['percent']}% ({v['vote']})", file = textfile)
    print("-----------------------------", file = textfile)
    print(f"Winner = {topCandidate}", file = textfile)



# ---------------------------------------------------------------------------------------------------------------------
# Previous Tries: Trail #1 and #2 would generate the correct answers
# but problematic when dealing with real-world big data.
# Like what if there are many more candidates?!
'''
# Trial No_2:
# Define variables as empty lists to hold values
Candidates = []
VoteCounts = []
PercentCounts = []
csvpath = os.path.join("..","Resources","election_data.csv")

# Create the looped row function: NOTE - not very efficient if there are even more candidates...
def processRow(PollData):
    # Create a new list to collect all candidates and votes
    if PollData[2] not in Candidates:
        Candidates[PollData[2]]={'vote':}
        Candidates.append(PollData[2])
        VoteCounts.append(int(1))
    # Add +1 to each voted candidate per row
    elif PollData[2] in Candidates[0]:
        VoteCounts[0] += 1
    elif PollData[2] in Candidates[1]:
        VoteCounts[1] += 1
    elif PollData[2] in Candidates[2]:
        VoteCounts[2] += 1
    elif PollData[2] in Candidates[3]:
        VoteCounts[3] += 1

    # Summarize the poll results into an organized dictionary of each candidates and their vote counts
    SummaryPoll = dict(zip(Candidates, VoteCounts))
    # Find the winner
    # Winner = max(SummaryPoll, key=SummaryPoll.get)

    # Create a dictionary for the percent votes
    PercentCounts = [round((i / TotalVotes * 100),2) for i in VoteCounts]
    PercentSummary = dict(zip(Candidates, PercentCounts))

# -----------------------------------------------------------------
# Trial No_1:
# Khan = VoteCounts[0]
# Correy = VoteCounts[1]
# Li = VoteCounts[2]
# OTooley = VoteCounts[3]
# PercentKhan = round((Khan / TotalVotes * 100),2)
# PercentCorrey = round((Correy / TotalVotes * 100),2)
# PercentLi = round((Li / TotalVotes * 100),2)
# PercentOTooley = round((OTooley / TotalVotes * 100),2)
# -----------------------------------------------------------------
# Results
with open("pyPoll_Final.txt", "w") as textfile:
    print("Election Results"#, file = textfile)
    print("-----------------------------"#, file = textfile)
    print(f"Total Votes: {TotalVotes}"#, file = textfile)
    print("-----------------------------"#, file = textfile)
    print(f"Khan: {PercentSummary['Khan']}% ({SummaryPoll['Khan']})"#, file = textfile)
    print(f"Correy: {PercentSummary['Correy']}% ({SummaryPoll['Correy']})"#, file = textfile)
    print(f"Li: {PercentSummary['Li']}% ({SummaryPoll['Li']})"#, file = textfile)
    print(f"O'Tooley: {PercentSummary["O'Tooley"]}% {SummaryPoll["O'Tooley"]}"#, file = textfile)
    print("-----------------------------"#, file = textfile)
    print(f"Winner: {Winner}"#, file = textfile)
    print("-----------------------------"#, file = textfile)
'''