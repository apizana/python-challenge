
#import modules
import os
import csv

#set path for file to collect data
csvpath = os.path.join("Resources", "budget_data.csv")

#set the output of the text file
text_path = "Final_Analysis.txt"

#set the output of the text filetext_path = "Final_Analysis.txt"
outfile = os.path.join("analysis", text_path)

#Set variables
totalmonths = []
profits = []
monthlyprofitchange = []

# Reaed in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header labels to iterate with the values   
    header = next(csvreader)

    # Iterate through the rows in the stored file contents        
    for row in csvreader:

        # Append the total month and total profit to their corresponding list
        totalmonths.append(row[0])
        profits.append(int(row[1]))

# Iterate through the profit in order to get the monthly change in profits
for i in range(len(profits) - 1):
        monthlyprofitchange.append(profits[i+1] - profits[i])
        total_months = len(totalmonths)
        sum_profits = sum(profits)
        avg_change = (round(sum(monthlyprofitchange) / len(monthlyprofitchange),2))

# Obtain the max and min of the monthly profit change list
max_increase = max(monthlyprofitchange)
max_decrease = min(monthlyprofitchange)


# Correlate max and min to the proper month using month list and index for max and min
# plus one at the end sinde month associated with change is the next month
max_increase_month = monthlyprofitchange.index(max(monthlyprofitchange)) + 1
max_decrease_month = monthlyprofitchange.index(min(monthlyprofitchange)) + 1

# Print the output to the terminal
output =(
        f"Financial Analysis\n"
        f"---------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${sum_profits}\n"
        f"Average Change: {avg_change}\n"
        f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase))})\n"
        f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease))})\n")

print(output)

#write changes to file
with open(outfile, 'w') as file:
        file.write("Financial Analysis")
        file.write("\n")
        file.write("---------------------")
        file.write("\n")
        file.write(f"Total Months: {total_months}")
        file.write("\n")
        file.write(f"Total: ${sum(profits)}")
        file.write("\n")
        file.write(f"Average Change: {round(sum(monthlyprofitchange) / len(monthlyprofitchange),2)}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(str(max_increase))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(str(max_decrease))})")