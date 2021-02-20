import os
import csv
import math

budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
profits_losses = 0
average_change = 0
previous_value = 0
has_previous_value = False
greatest_increase = -math.inf
greatest_increase_date = "doesn't exist"
greatest_decrease = math.inf
greatest_decrease_date = "doesn't exist"

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   # print(csvreader)

        
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
        
    for row in csvreader:
        #print(row)

        total_months += 1
    

        profits_losses += int(row[1])
    

        if has_previous_value:
            current_change = int(row[1]) - previous_value
            average_change += current_change
            previous_value = int(row[1])
            
            if greatest_increase < current_change:
                greatest_increase = current_change
                greatest_increase_date = row[0]
            if greatest_decrease > current_change:
                greatest_decrease = current_change
                greatest_decrease_date = row[0]
        else:
            previous_value = int(row[1])
            has_previous_value = True

    result = "Financial Analysis\n"
    result += "-------------------------------\n"
    result += f"Total months: {total_months}\n"
    result += f"Total: ${profits_losses}\n"
    result += f"Average Change: ${round(average_change/(total_months-1),2)}\n"
    result += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    result += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    result += "---\n"


    print(result)

    with open("result.txt", "w") as text_file:
            text_file.write(result)
        
        



