# Modules
import os
import csv
# Define variables
biggestLoss = None
biggestGain = None
prevRowData = None
totalRev = 0
totalMonthlyChg = 0
# Set CSV path for pyBank file
csvpath = os.path.join("..","Resources","budget_data.csv")

def processRow(data):
    # set local variables to link up to the defined global variables
    global totalRev, biggestLoss, biggestGain, prevRowData, totalMonthlyChg
    # Add up total revenue per row
    totalRev += int(data[1])
    # Collect the first row of data
    if prevRowData is None:
        prevRowData = data
    # Perform calculations to compare current row with previous row
    else:
        diff = int(data[1]) - int(prevRowData[1])
        totalMonthlyChg += diff
        if biggestGain is None:
            biggestGain = [data[0], data[1], 0]
        elif diff > biggestGain[2]:
            biggestGain = [data[0], data[1], diff]
        if biggestLoss is None:
            biggestLoss = [data[0], data[1], 0]
        elif diff < biggestLoss[2]:
            biggestLoss = [data[0], data[1], diff]
    # Re-define row
    prevRowData = data

# Open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Skip the header row
    csv_header = next(csvreader)
    # print(f"{csv_header}")

    # Add up the total dates
    totaldates = 0
    for row in csvreader:
        # print(row)
        totaldates += 1
        processRow(row)
    # Calculate average change
    avgChange = totalMonthlyChg/(totaldates-1)

# Results
with open("pyBank_Final.txt", "w") as textfile:
    print("Financial Analysis", file = textfile)
    print("-------------------", file = textfile)
    print(f"Total Months: {totaldates}", file = textfile)
    print(f"Total: ${totalRev}", file = textfile)
    print(f"Average Change: ${round(avgChange,2)}", file = textfile)
    print(f"Greatest Increase in Profits: {biggestGain[0]} (${biggestGain[2]})", file = textfile)
    print(f"Greatest Decrease in Profits: {biggestLoss[0]} (${biggestLoss[2]})", file = textfile)
