# Import drive, csv file type, and systems to read/write terminal output to txt file
import os
import csv
import sys

# Import csv file
filepath = os.path.join("Resources","Financial_Data.csv")

# Create empty lists to store CSV data
date = []
pl_total = []
pl_change = []

# Read file, seperate the items by comma, skip header to calculate results accurately
with open (filepath, 'r', encoding = 'utf-8') as pybank_data:
    csvreader = csv.reader(pybank_data, delimiter =",")
    header = next(csvreader, None)
    # Add items into the above list as per the csv columns
    for row in csvreader:
        date.append(row[0])
        pl_total.append(int(row[1]))

# Ensure items of the list are correct
# print(date)
# print(pl_total)

# Calculate P&L differences between rows/months 
    # Need to determine from 1 to the last item of the row. 
    # We can get last row number by setting the length of the last row of pl_total which is len(pl_total)
    # For Loop needed to calculate the pl_change from the 2nd row to 1st row, 3rd row to 2nd row, etc

for i in range(1,len(pl_total)):
        # Determine pl_change
        pl_change.append(int(pl_total[i]) - int(pl_total[i-1]))
        # Determine pl_change average, max and min upon caculating the pl_change list
        pl_change_avg = round(sum(pl_change)/len(pl_change),2)
        pl_change_max = max(pl_change)
        pl_change_min = min(pl_change)
        # Find the month of max and min by looking at the index function
        pl_change_max_date = str(date[pl_change.index(max(pl_change))])
        pl_change_min_date = str(date[pl_change.index(min(pl_change))])

# Print to Terminal
print("Finanacial Summary")
print("--------------------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total:  ${sum(pl_total)}")
print(f"Average Change:  ${pl_change_avg}")
print(f"Greatest Increase in Profits:  {pl_change_max_date} $({pl_change_max})")
print(f"Greatest Decrease in Profits:  {pl_change_min_date} $({pl_change_min})")

#Output to txt file
stdoutOrigin=sys.stdout 
sys.stdout = open("Financial_Summary.txt", "w")

print("Finanacial Summary")
print("--------------------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total:  ${sum(pl_total)}")
print(f"Average Change:  ${pl_change_avg}")
print(f"Greatest Increase in Profits:  {pl_change_max_date} $({pl_change_max})")
print(f"Greatest Decrease in Profits:  {pl_change_min_date} $({pl_change_min})")


sys.stdout.close()
sys.stdout=stdoutOrigin


